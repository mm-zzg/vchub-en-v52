# Management Platform

 In order to allow the configurator to focus on the configuration, VC Hub has grouped all other configuration-related tasks into our Management Panel. Before starting your configuration, you need to configure your project in the Management Panel.

 Below you will find a list of important features of the VC Hub Management Panel, which can be accessed by clicking on the corresponding links.

| **Feature**       | **Description**   |
|-------------------|-------------------|
| [Projects ](projects/index.md)                                  | VC Hub allows you to create several configuration projects at the same time, each of which can contain its own individual screen, but all of which share all of the management platform's configurations, such as tags, device connections, database connections, and network configurations.  |
| [Devices](devices/index.md)                          | Devices are the field devices that you need to connect to when configuring your project. VC Hub can connect your various devices via MQTT protocols.  |
| [Tags](assets-and-tags/index.md)                            | Different devices have different address spaces. To deal with this difference, VC Hub provides the concept and functionality of assets and tags, which are associated with the VC Hub platform and not with the device (protocol), but a tag can be bound to the address of various devices by binding. What's more, VC Hub supports the asset-based construction of your tag system so that it matches the physical model of your actual field device, making it easy to manage and operate.   |
|[Alarming](alarming/index.md)                   | Alarming are an important and indispensable feature of VC Hub  systems, and VC Hub provides you with industry-standard alarms, but before you can configure alarms, you need to configure some alarms in the management platform. For example, alarms need to be stored eventually, in order to store them, you need to configure the alarms with an history storage.  In addition, you can also configure the duration of stale alarms.    |
|[Scripts](scripts/index.md)                 | Scripts is an advanced feature of the VC Hub system that allows you to realize complex business scenarios that are not possible with the configuration, e.g. if you need logic algorithms for tags, VC Hub uses Javascript as a simple and efficient scripting language and provides support for scripting in multiple scenarios. The scripts that you configure in the administration platform are run on the server (VC Hub runs on the server as a Web Server), such as tag change scripts, cycle scripts, and schedules (running scripts in the form of schedules). Of course, we also provide you with scripting functions that are relevant to your configuration, such as control scripts, action scripts, and so on.   | 
| [Security](security/index.md)                                | VC Hub provides a security-based role management system that allows you to build various roles for your field applications, such as Engineer, Operator, Maintenance, and so on. For your convenience, VC Hub also gives you several built-in roles for direct use.  |
|[AI](ai/index.md)   | Configure Models and Prompts for the AI Assistant. Models provide the AI capabilities, while Prompts define instructions for specific business scenarios. The configured Models and Prompts can be selected when using the AI Assistant.  |
| [Diagnostics](diagnostics/index(saas).md)                              | VC Hub is a complex system involving various aspects, so in order to monitor and diagnose the VC Hub system itself, it provides a wealth of diagnostics functions. For example, you can use the diagnostics to check in real time the CPU and memory occupied by the VC Hub system.   |



