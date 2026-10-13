# Write Mode-Specific Documentation

## Overview

This guide explains how to maintain documentation for the **on-premise** and **SaaS** build modes. The on-premise mode is the default.

Most documents should be shared. Create mode-specific files or folders only when the instructions, screenshots, or supporting assets differ between deployments.

## Choose a Content Structure

Use the following order of preference:

1. Use one shared document when both modes can use the same content.
2. Use file variants when one document differs between modes.
3. Use folder variants when several documents or their assets differ between modes.

## Write Shared Content

A normal path without a mode suffix is included in both modes:

```text
docs/installation/configure-network.md
```

Add its normal path to the navigation:

```yaml
- installation/configure-network.md
```

## Create File Variants

Add the mode suffix immediately before `.md`:

```text
docs/quick-start/index(on-premise).md
docs/quick-start/index(saas).md
```

Both source files are published at the same canonical path:

```text
quick-start/index.md
```

Add only the canonical path to `nav` in `mkdocs.yml`:

```yaml
- Quick Start: quick-start/index.md
```

Never add a suffixed source path to the navigation.

### Create a page for one mode only

Create only the applicable variant:

```text
docs/installation/local-service(on-premise).md
```

In this example:

- The on-premise site publishes `installation/local-service.md`.
- The SaaS site does not publish the page.
- The build removes `installation/local-service.md` from the SaaS navigation.

The same behavior applies when only the SaaS variant exists.

## Create Folder Variants

Add the mode suffix to the folder name when a group of pages or its supporting files differs:

```text
docs/deployment(on-premise)/index.md
docs/deployment(on-premise)/service-account.md
docs/deployment(on-premise)/images/topology.png

docs/deployment(saas)/index.md
docs/deployment(saas)/tenant-settings.md
docs/deployment(saas)/images/topology.png
```

The selected folder is published without the suffix:

```text
deployment/index.md
deployment/service-account.md
deployment/tenant-settings.md
deployment/images/topology.png
```

Only files present in the selected mode are published. Navigation entries for pages available only in the other mode are removed automatically.

Always use canonical paths in `mkdocs.yml`:

```yaml
- Deployment:
    - deployment/index.md
    - deployment/service-account.md
    - deployment/tenant-settings.md
```

### Use assets in folder variants

Assets inside a mode-specific folder are mapped to the canonical folder. Author links as if the suffix does not exist:

```markdown
![Deployment topology](images/topology.png)
```

Prefer a shared asset outside mode-specific folders when both modes use the same image or download.

## Write Links

Always link to canonical document paths, not physical variant filenames or folders.

Correct:

```markdown
[Configure deployment](../deployment/index.md)
```

Incorrect:

```markdown
[Configure deployment](../deployment(saas)/index.md)
[Configure deployment](../deployment/index(saas).md)
```

A link from shared content to a mode-only page will be broken in the mode where that page is unavailable. Avoid such links, or move the referring content into the same mode-specific variant.

## Avoid Naming Conflicts

Do not combine a canonical document with variants of the same document:

```text
docs/quick-start/index.md
docs/quick-start/index(on-premise).md
```

Do not create two paths that map to the same canonical path in one mode:

```text
docs/deployment(on-premise)/index.md
docs/deployment/index(on-premise).md
```

Do not mix different mode suffixes in one path:

```text
docs/deployment(saas)/setup(on-premise).md
```

These conflicts stop the build so that one source cannot silently overwrite another.

## Update Navigation

1. Determine the canonical path by removing `(on-premise)` or `(saas)` from file and folder names.
2. Add the canonical `.md` path to `nav` in `mkdocs.yml`.
3. Add each logical page only once, even when both variants exist.
4. Keep the entry in the position where it should appear in either mode.

If the selected mode does not contain a corresponding page, the build removes that page entry. Sections left empty by this process are also removed.

## Preview Both Modes

In VS Code:

1. Press **Ctrl+Shift+P**.
2. Select **Tasks: Run Task**.
3. Select **Preview docs: both modes**.
4. Open the on-premise site at `http://127.0.0.1:8000`.
5. Open the SaaS site at `http://127.0.0.1:8001`.

Individual **Preview docs: on-premise** and **Preview docs: SaaS** tasks are also available.

## Verify a Change

Check all of the following before submitting a change:

- The shared or selected variant appears in the expected mode.
- The opposite variant is absent from navigation, search, and direct output.
- URLs do not contain `(on-premise)` or `(saas)`.
- Navigation uses canonical paths only.
- Internal links use canonical paths and resolve in every applicable mode.
- Images and downloads are available in every mode that displays the referring page.
- Both preview builds complete without new warnings or errors.

## Troubleshooting

!!! warning "A navigation entry is shown as a missing link"
    Confirm that `mkdocs.yml` uses the canonical path. For example, use `quick-start/index.md`, not `quick-start/index(saas).md`.

!!! warning "The build reports a canonical document conflict"
    A normal file and a mode-specific variant map to the same path. Remove the normal file or replace it with the missing mode variant.

!!! warning "The build reports conflicting mode suffixes"
    A path contains both `(on-premise)` and `(saas)`. Use one mode consistently throughout the complete path.

!!! warning "A page is available but an image is missing"
    Move the image into both mode-specific folders, or place one shared image at a normal canonical path and update the Markdown link.

## Naming Reference

| Purpose | Source naming | Navigation path |
| --- | --- | --- |
| Shared page | `abc/page.md` | `abc/page.md` |
| Paired file variants | `abc/page(on-premise).md` and `abc/page(saas).md` | `abc/page.md` |
| On-premise-only page | `abc/page(on-premise).md` | `abc/page.md` |
| SaaS-only page | `abc/page(saas).md` | `abc/page.md` |
| Paired folder variants | `abc(on-premise)/page.md` and `abc(saas)/page.md` | `abc/page.md` |
| On-premise-only folder | `abc(on-premise)/page.md` | `abc/page.md` |
| SaaS-only folder | `abc(saas)/page.md` | `abc/page.md` |