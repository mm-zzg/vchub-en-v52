# Asset

 There can be any number of assets in VC Hub, and the user can create tags to be maintained in any asset. Assets can be viewed as containers for tags, and the tags in each asset are isolated from each other, and the tags are dependent on the asset for their existence in the system. 

 All tags are available in the asset, provide real-time values, and support historical data storage.

## **Add**

Click "**Tags** "->"**Asset** "menu to enter the asset management page.

Users can add new assets by clicking the "Add" button in the upper right corner and filling in the asset information.

![alt text](1.png)

**Configuration items**

| **Configuration** | **Description**   |
|-------------------|--------------|
| Name              | The name of the asset, the name cannot be repeated, required.  |
| Description       | Description of the asset,optional. |

## **Query**

 After  entering the asset m anagement page, users can view all the assets under the current workspace, which are sorted in reverse chronological order by default,and users can customize the sorting according to their needs.

 Users can do fuzzy query on the asset name through the input box in the upper right corner.

## **Edit**

 Users can modify the asset information by clicking the "Modify" button on the right side of any asset in the asset list. Once an asset is created, its asset type cannot be modified.

## **Manage Tags**

This function is used to manage all tags under the Asset.

Clicking the button will open a new browser window displaying the Asset Tree. The Asset Tree  provides the same functionality as the Asset window in the 2D Designer.

![alt text](5.png)

## **Delete**

 Users can click the "Delete" button on the right side of any asset in the asset list to delete the selected asset. After clicking the button, a prompt box will pop up, and users can click OK to delete the asset. Note that when the asset is deleted, all models, instances and tags under the asset will be deleted together.

 The **System** Asset cannot be deleted.

 ![alt text](4.png)

## **Export**

 Users can click the "Export" button on the right side of any asset in the asset list to export the asset configuration and all models, instances and tags under the selected asset to a Json file.

 Note that it is not recommended to modify the Json file if you don't understand its contents.

## **Import**

 With  the "Import" button on the top right corner of the page, users can import the Json file into the system again. If there is a renamed asset in the current system, users will be prompted to change the name.

  


