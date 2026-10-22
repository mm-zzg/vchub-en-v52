# Windows Environment 

VC Hub provides installation packages for the 64-bit Windows operating system.

Recommended Systems for Installation:

- Windows Server 2012 R2
- Windows Server 2016
- Windows Server 2019
- Windows Server 2022
- Windows 10  (Not supported in Home Edition)
- Windows 11  (Not supported in Home Edition)

## **Installation Steps**

1. Run the installation package program as an administrator.
2. Select the installation language. <br>
      ![alt text](5.png)
3. Perform a port check, if the port is occupied, the installation cannot proceed. <br>
      ![alt text](6.png)
4. Read and accept the license agreement. <br>
      ![alt text](7.png)
5. Choose the installation location; the default path is: "C:\Program Files\WAGO Visualization And Control Hub". <br>
      ![alt text](8.png)
6. Select the VC Hub application data directory. <br>
      ![alt text](9.png)
7. Prepare for installation. <br>
      ![alt text](10.png)
8. The installation is complete. <br>
      ![alt text](11.png)
9. After completion, the default access to the VC Hub site is: `http://localhost:8066`. After the installation, you will enter the configuration wizard interface.

## **Configuration Steps**

1. Create an administrator user. Remember this username and password, as you will use them to log in for the first time. <br>
      ![alt text](12.png)
2. Port configuration, configure HTTP, HTTPS ports, and remember the access port. <br>
      ![alt text](13.png)
3. Configure HTTPS connection and certificate. <br>
      ![alt text](52.png)   
4. After completing the above steps, wait for the program to load, and then you can log in to the default-created workspace with the user created in step 1.

**Note**:

After each installation, a new empty workspace will be created by default. To return to the original workspace, you need to log in to the new workspace first and then manually open the original workspace from the workspace list.

## **Service Security**

The installer automatically configures the VC Hub Windows service to run under the dedicated virtual service account `NT SERVICE\WAGO_Visualization_And_Control_Hub`. It also grants the service only the application and data directory permissions required at runtime.

Do not create a regular local user for the service, change the service to run as `LocalSystem`, or grant it administrator privileges.

For details and verification steps, see [VC Hub Service Account and File Permissions](setup-service-running-user.md).

## **TLS Cipher Suite Hardening (Recommended)**

VC Hub enforces TLS 1.2 and TLS 1.3 only at the application level — legacy and insecure protocols including TLS 1.0, TLS 1.1, SSLv2, and SSLv3 are already disabled in code.

However, on Windows, cipher suites are controlled by the Windows SChannel security provider and cannot be restricted directly through the application code. Therefore, cipher suite hardening must be performed at the operating system level using Windows Group Policy to allow only strong forward‑secret cipher suites and disable insecure or legacy suites.

### Why is this necessary?

Modern security standards recommend restricting TLS communication to strong cipher suites. Allowing weak cipher algorithms (such as static RSA key exchange `TLS_RSA_*`) increases the risk of downgrade attacks and weak encryption usage. Configuring the SSL Cipher Suite Order ensures that only secure cipher suites with forward secrecy are used for HTTPS connections.

### Configuration Steps

1. Press `Win + R`, type `gpedit.msc` and press Enter to open the **Local Group Policy Editor**.
![alt text](42.png)
2. Navigate to: **Computer Configuration** → **Administrative Templates** → **Network** → **SSL Configuration Settings**.
3. Double-click **SSL Cipher Suite Order** in the right pane.
4. Select **Enabled**.
5. In the **SSL Cipher Suites** text box, replace the existing content with the following recommended cipher suite order:

```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_AES_256_GCM_SHA384,TLS_AES_128_GCM_SHA256,TLS_CHACHA20_POLY1305_SHA256
```

6. Click **OK** to save.
![alt text](43.png)
7. Restart the server or run `gpupdate /force` in an elevated command prompt for the policy to take effect.

### Allowed Cipher Suites

**TLS 1.2** — only the following forward‑secret cipher suites should be permitted:

| Cipher Suite | Key Exchange | Encryption |
|---|---|---|
| TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 | ECDHE | AES-256-GCM |
| TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 | ECDHE | AES-128-GCM |

**TLS 1.3** — Only the following cipher suites are permitted (TLS 1.3 is only supported on Windows 11 and Windows Server 2022 or later):

- TLS_AES_256_GCM_SHA384
- TLS_AES_128_GCM_SHA256
- TLS_CHACHA20_POLY1305_SHA256

### Notes

- Back up the original cipher suite order before making changes.
- Incorrect configuration may prevent older clients or browsers from connecting. Verify compatibility with your environment before applying.
- On Linux deployments, cipher suite restriction is handled automatically by the application code — no manual OS‑level configuration is required.

## **Uninstallation Steps**

1. Enter the software uninstall list from the Control Panel. Find VC Hub and proceed with the uninstallation.
      ![alt text](15.png)
2. Confirm the uninstallation to complete the removal of the application.
      ![alt text](16.png)


