# Cloud Version

## 1. Subscribe to VC Hub

TODO







## 2. Start working with VC Hub

### 2.1 Create a Project

Click the "Add" button in the project list to create a project.

![alt text](1.png)

### 2.32 Add Assets

After the installation of VC Hub, a default asset will be automatically created, which you can use for basic testing. You can also click "Tags" -> "[Assets](../management-platform/assets-and-tags/asset/index.md)" page and then click the "New" button to create new assets.

### 2.3 Open the Editor

On the project list page, click the "Design" button for the project.

![alt text](2.png)

Open the configuration editor to display the following interface.

![alt text](3.png)

### 2.4 Create a New Page

Click "New Page" to quickly create a new page.

![alt text](4.png)

In the **Tools** window on the left side of the designer, add for example "Rect" , "Label" , "Value Display",and "Historical Trend Chart" controls to the page. You can also use the search functionality.

![alt text](5.png)

### 2.5 Create a Tag

In the asset dropdown box of the asset window in the configuration editor, select an asset and then click the add button to add a memory tag to that asset. Tag name: liquid.

![alt text](6.png)

Enable the simulated property for this tag, using simulated value as the tag value. Types supported are **Random**, **Increment**, **Decrement**, and **Fixed.**

![alt text](7.png)

### 2.6 Enable History for Tags

At the top of the tag editing page, enable [history](../management-platform/assets-and-tags/tag/tag-properties/history.md) to store the value of the tag historically.

![alt text](8.png)

### 2.7 Bind Tag

Bind tags to controls on the page.

1. Set the display content of the text label to: "Liquid level:"
    ![alt text](9.png)
2.  In the animation of the rectangle, select the fill animation. Click the value binding button and bind the created tag:liquid.
    ![alt text](10.png)
3. In the value display control, click the value binding button and bind the created tag:liquid. Afte binding, the binding icon will turn from gray to green.
    ![alt text](11.png)
4. In the historical chart control, click the value binding button and bind the created tag:liquid. 
    ![alt text](12.png)
    
**Note:** For more information on binding, please refer to the Property Binding page. 

### 2.8 Preview/Run

Click the preview button in the page tool bar to view the preview effect. You can also click the run button for the project in the project list to view the running page.

![quick-start-guide](../assets/images/quick-start-guide.gif)







