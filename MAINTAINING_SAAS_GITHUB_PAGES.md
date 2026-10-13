# Provision the SaaS GitHub Pages Deploy Key

## Overview

This guide explains how a repository maintainer uses `.github/workflows/provision-saas-deploy-key.yml` to create and configure SSH authentication for the SaaS documentation deployment.

The provisioning workflow automatically:

1. Generates a dedicated Ed25519 SSH key pair.
2. Stores the private key as the `SAAS_DEPLOY_KEY` Actions secret in the source repository.
3. Stores the public key as the `SAAS_DEPLOY_PUBLIC_KEY` Actions variable in the source repository.
4. Registers the public key as a writable deploy key in the SaaS repository.
5. Removes the temporary key files from the GitHub-hosted runner.

The target repository is derived from `${{ github.repository }}-saas`. For example:

| Purpose | Repository |
| --- | --- |
| Source repository | `mm-zzg/vchub-en-v52` |
| Derived SaaS repository | `mm-zzg/vchub-en-v52-saas` |

## Prerequisites

Before running the provisioning workflow, verify that:

- The `${CurrentRepositoryName}-saas` target repository already exists.
- The target repository belongs to the same owner as the source repository.
- You have administrator access to both repositories.
- GitHub Actions is enabled in the source repository.

## Create the Bootstrap Token

The normal workflow `GITHUB_TOKEN` cannot create repository secrets, variables, or deploy keys. Create a temporary fine-grained personal access token for provisioning.

1. Open your GitHub account settings.
2. Select **Developer settings** > **Personal access tokens** > **Fine-grained tokens**.
3. Select **Generate new token**.
4. Set a short expiration time.
5. Select both the source repository and the `${CurrentRepositoryName}-saas` target repository.
6. Configure these repository permissions:

    | Permission | Access |
    | --- | --- |
    | Secrets | Read and write |
    | Variables | Read and write |
    | Administration | Read and write |
    | Metadata | Read-only |

7. Generate the token and copy it immediately.

!!! warning
    Treat the bootstrap token as a temporary administrator credential. Do not commit it, paste it into workflow YAML, or share it in an issue.

## Store the Bootstrap Token

Add the temporary token to the source repository:

1. Open the source repository on GitHub.
2. Select **Settings**.
3. Select **Secrets and variables** > **Actions**.
4. On the **Secrets** tab, select **New repository secret**.
5. Enter `DEPLOY_KEY_BOOTSTRAP_TOKEN` as the name.
6. Paste the fine-grained token as the value.
7. Save the secret.

The workflow reads this secret as `GH_TOKEN`. It is used only to create the deployment secret, public-key variable, and target deploy key.

## Run the Provisioning Workflow

1. Open the source repository on GitHub.
2. Select **Actions**.
3. Select **Provision SaaS deploy key** from the workflow list.
4. Select **Run workflow**.
5. Select the source branch containing `.github/workflows/provision-saas-deploy-key.yml`.
6. Select **Run workflow** to confirm.
7. Open the workflow run and wait for the **Generate and register deploy key** step to complete.

A successful run ends with a message similar to:

```text
Configured a writable deploy key for OWNER/CURRENT_REPOSITORY-saas
```

Re-running the workflow rotates the key. It removes a target deploy key named `saas-pages-deploy-key`, generates a new pair, and replaces the source secret and variable.

## Verify the Provisioned Key

### Verify the private-key secret

In the source repository:

1. Open **Settings** > **Secrets and variables** > **Actions**.
2. Select the **Secrets** tab.
3. Confirm that `SAAS_DEPLOY_KEY` exists.

GitHub does not display the stored private-key value after creation.

### Verify the public-key variable

In the source repository:

1. Open **Settings** > **Secrets and variables** > **Actions**.
2. Select the **Variables** tab.
3. Confirm that `SAAS_DEPLOY_PUBLIC_KEY` exists and begins with `ssh-ed25519`.

The variable is informational and is not used for authentication.

### Verify the target deploy key

In the `${CurrentRepositoryName}-saas` repository:

1. Open **Settings** > **Deploy keys**.
2. Confirm that `saas-pages-deploy-key` exists.
3. Confirm that it is marked **Read/write**.

The public value should match `SAAS_DEPLOY_PUBLIC_KEY` in the source repository.

## Remove the Bootstrap Credential

After successful verification:

1. Delete `DEPLOY_KEY_BOOTSTRAP_TOKEN` from the source repository's Actions secrets.
2. Revoke or delete the fine-grained personal access token in your GitHub account settings.

The regular documentation deployment does not need the bootstrap token. It uses only `SAAS_DEPLOY_KEY`.

!!! warning
    Do not leave the bootstrap token active after provisioning. It has broader permissions than the SSH deploy key used by the documentation workflow.

## Configure GitHub Pages

After the first successful SaaS documentation deployment:

1. Open the `${CurrentRepositoryName}-saas` repository.
2. Select **Settings** > **Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Select the `gh-pages` branch.
5. Select `/ (root)` as the folder.
6. Save the configuration.

The Pages URL normally follows this format:

```text
https://OWNER.github.io/CURRENT_REPOSITORY-saas/
```

## Run the Documentation Deployment

The workflow in `.github/workflows/ci.yml` uses `SAAS_DEPLOY_KEY` to:

1. Configure SSH on the GitHub-hosted runner.
2. Add `git@github.com:OWNER/CURRENT_REPOSITORY-saas.git` as the `docs-target` remote.
3. Build the documentation with `DOCS_BUILD_MODE=saas`.
4. Push the generated site to the target repository's `gh-pages` branch.

Push a change to `main` or `master`, then verify that:

- The **Configure SSH access to SaaS repository** step succeeds.
- The **Deploy SaaS documentation to target repository** step succeeds.
- The target repository's `gh-pages` branch is updated.
- The target GitHub Pages site displays the SaaS content.

## Rotate the Deploy Key

To rotate the key:

1. Create another temporary fine-grained token with the required permissions.
2. Store it as `DEPLOY_KEY_BOOTSTRAP_TOKEN`.
3. Run **Provision SaaS deploy key** again.
4. Verify the new source secret, variable, and target deploy key.
5. Delete the bootstrap secret and revoke the temporary token.
6. Run the documentation deployment to test the new key.

## Troubleshooting

### `DEPLOY_KEY_BOOTSTRAP_TOKEN is not configured`

The source repository does not contain the bootstrap secret, or the workflow cannot access it. Create the secret at repository level and run the workflow from the source repository.

### `HTTP 403: Resource not accessible by personal access token`

Confirm that the bootstrap token:

- Includes both source and target repositories.
- Has **Secrets: Read and write**.
- Has **Variables: Read and write**.
- Has **Administration: Read and write**.
- Is not expired or revoked.
- Has organization authorization if single sign-on is required.

### `HTTP 404: Not Found`

Confirm that `${CurrentRepositoryName}-saas` exists under the same repository owner. If the target uses another name or owner, update `TARGET_REPOSITORY` in both workflows.

### `Key is already in use`

A GitHub deploy key can be attached to only one repository. Delete the existing copy of that public key or rerun the workflow to generate a new key pair.

### The deploy key is read-only

Open the target repository's deploy-key settings and verify that `saas-pages-deploy-key` has write access. The provisioning workflow submits it with `read_only=false`.

### Deployment reports `Permission denied (publickey)`

Verify that:

- `SAAS_DEPLOY_KEY` exists in the source repository.
- `saas-pages-deploy-key` exists in the target repository.
- The target deploy key matches `SAAS_DEPLOY_PUBLIC_KEY`.
- The target deploy key has write access.
- Repository rules allow the key to update `gh-pages`.
