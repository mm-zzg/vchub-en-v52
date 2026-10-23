# New in this Version

## AI Assistant

VC Hub introduces an AI Assistant to simplify script development and visualization design, helping users create functional scripts and customized runtime pages with less manual effort.

In the Script Editor, users can describe their requirements in natural language and provide relevant tag information to generate scripts automatically. This helps reduce the effort required to write scripts manually and makes script development more accessible to users with limited programming experience.

In the HTML Viewer control, the AI Assistant can generate visually appealing runtime pages based on user descriptions and selected data sources. Users can create customized interfaces more efficiently without having to build every element from scratch.

## German Language Support

VC Hub now supports German in addition to the existing system languages. Users can select German as the system language to interact with the application in German.

This enhancement provides a more localized user experience, improves accessibility for German-speaking users, and better accommodates language preferences in different regions.


## Enhanced WAGO Protocol Compatibility

VC Hub extends its WAGO Protocol support with additional capabilities for data organization, command execution, and communication.

The following enhancements are included:

- Hierarchical Collections: Supports hierarchical collections to represent and organize data in a structured manner.

- Custom Commands: Supports custom WAGO Protocol commands to accommodate application-specific communication requirements.

- Built-in Commands: Supports built-in WAGO Protocol commands for accessing predefined protocol functionality.

- Handshake Mechanism: Supports WAGO Protocol communication with a handshake mechanism to accommodate communication scenarios that require a handshake.

You can execute these commands in the control's Event configuration.

These enhancements expand the range of supported WAGO Protocol configurations and provide greater flexibility when integrating devices and implementing communication workflows.

## Integration with WAGO Solutions Platform

VC Hub can now be integrated into the WAGO Solutions Platform, enabling cloud-based deployment and centralized platform management.

The integration introduces platform-managed application instances and supports tenant-aware lifecycle management. Each tenant's VC Hub instance can be managed through the platform, providing a consistent approach to application deployment and operation across multiple tenants.

Identity and access management are integrated with the Solutions Platform, allowing user access to be managed in accordance with platform roles and permissions. Secure access mechanisms support the operation of VC Hub within a multi-tenant cloud environment.

## Workspace File Signing and Verification

VC Hub introduces workspace file signing and verification to help protect workspace authenticity and integrity during export, transfer, and import.

When exporting a workspace, users can sign the file using an appropriate signing certificate. During import, VC Hub verifies the workspace signature to determine whether the file has been modified and whether its signing certificate is trusted and valid.

If the signature cannot be verified or the signing certificate is not trusted or valid, the import process is rejected. Users can import the required public certificate into the Trust Store or export the workspace again using a valid signing certificate before retrying.

This mechanism helps prevent unauthorized workspace modifications and supports secure workspace exchange both within the same system and between different system instances.


## SMS Abuse Prevention

VC Hub enhances the security of SMS alarm notifications to help reduce the risk of excessive SMS usage and misuse of external SMS providers.

Alarm notifications can be sent through configured SMS providers, such as Twilio and Ali Cloud. Repeated alarm triggers, whether accidental or malicious, may result in excessive SMS consumption, unexpected costs, or exhaustion of the available SMS quota. This could prevent subsequent critical alarm notifications from reaching their intended recipients.

The enhanced security measures help mitigate the risks associated with SMS abuse and excessive usage, supporting more reliable delivery of important alarm notifications and better control over SMS-related costs.

## File Upload Size Limit

VC Hub introduces file size limits for upload operations to prevent excessively large files from being uploaded.

This enhancement helps control resource consumption, reduce the risk of excessive storage and memory usage, and improve system stability during file uploads.

Users must ensure that uploaded files comply with the applicable size limits.

## Complete Data Removal During Uninstallation

VC Hub enhances the uninstallation process by providing an option to remove the application's data directory in addition to uninstalling the application itself.

The data directory may contain configuration files, cached data, logs, and downloaded assets. Depending on the selected uninstallation option, users can remove these files to free up disk space and prevent residual data from remaining on the system.

This enhancement also helps avoid unexpected behavior caused by outdated configuration files during reinstallation and provides users with greater control over the removal of locally stored data.

## Login Attempt Delay

VC Hub introduces a delay mechanism after repeated failed login attempts to strengthen protection against brute-force attacks.

When multiple consecutive login attempts fail, the system applies a delay before allowing subsequent login attempts. This makes automated password-guessing attacks more difficult and helps protect user accounts against unauthorized access.

The mechanism adds an additional layer of security to the login process while preserving the normal authentication workflow for legitimate users.