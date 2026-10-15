# System Tag

System tags are used to display current system related status information, such as alarm data, memory usage, performance indicators, etc. System tags cannot be deleted or modified.

You can view the detailed system tags by selecting the asset named "System" in the Asset window.

![alt text](9.png)

The system tags contain the Client and Server directories.

**Client**: The device that the user uses to log on to VC Hub, such as an office computer;

**Server**: The device on which VC Hub is installed.

The **Client** directory contains Username and Role. **Read-only**, not editable.

![alt text](10.png)

| **Name** | **Description**    | **Data Type** |
|----------|-------|---------------|
| Username | The user name of the current login，e.g. Sam | String   |
| Role     | The role of the current login, e.g. Admin   | String  |

The Server folder contains the following tags:

![alt text](11.png)

The details are shown in the following table:

| **Name**   | **Description**    | **Data Type** |
|-----------|------------|---------------|
| CurrentDateTime  | The time of the server where the current system is located.   | DateTime      |
| Timezone  | The time zone of the current server.  | String        |
| **Alarm**     |    |    |
| ActiveAcked   | The number of alarms that are currently active and acknowledged.  | Integer       |
| ActiveUnacked   | The number of alarms that are currently active and unacknowledged.     | Integer       |
| ClearUnacked    | The number of alarms that are currently in the cleared, unacknowledged   | Integer       |
| **Devices**(One separate folder per device type. Each device is displayed as a separate folder under each device type folder, and 2 system tags are displayed under the device folder: Connected, Enabled.) |    |               |
| Connected   | The current connection status of the device, connected is shown as true, unconnected is shown as false.  | Bool          |
| Enabled  | The current enabled state of the device is shown as true for enabled and false for disabled, and can be enabled and disabled in the “Enabled State” column of the device list.  MQTT Native and WAGO Protocol devices only have the Enabled tag.                  | Bool          |


The system tags under the **Server** directory support editing. **Double-click** a tag or select **"Edit"** from the right-click menu to open the **edit window**.

![alt text](12.png)



