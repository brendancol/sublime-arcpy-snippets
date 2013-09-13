
sublime-arcpy-snippets
======================

**Collection of Sublime Text snippets for esri arcpy library**

###Installation
1. fork / clone repository (git clone https://github.com/brendancol/sublime-arcpy-snippets)
2. clone into local Sublime "User" folder
  * **Windows:** C:\Users\<user>\AppData\Roaming\<Sublime Text 2 or 3>\Packages\User.
3. Done...




###Keyboard Triggers
| Snippet        | Trigger           | Description  | Scope| 
| ------------- |-------------| -----| -----|
|arcpy-create-feature-class |GP Create Feature Class |Template for create a new feature class (arcpy.CreateFeatureclass_management) | source.python| 
|arcpy-get-count |GP Get Count |gets integer count(arcpy.GetCount_management) | source.python| 
|arcpy-join-field |GP Join Field |Joins the contents of a table to another table based on a common attribute field.  This is a permanent join. | source.python| 
|arcpy-make-feature-layer |GP Make Feature Layer |Creates a feature layer from an input feature class or layer file. The layer that is created by the tool is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved. | source.python| 
|arcpy-search-cursor |searchCursor |open search cursor on feature class (arcpy.da.SearchCursor) | source.python| 
|arcpy-select-layer-by-attribute |GP Select Layer By Attribute |Adds, updates, or removes a selection on a layer or table view based on an attribute query. | source.python| 
|arcpy-update-cursor |updateCursor |open update cursor (arcpy.da.UpdateCursor) | source.python| 
|toolbox-tool |toolpyt |Tool template for Python Toolbox (.pyt) | source.python| 
|unittest-testcase |testCase |Adds python unittest test case | source.python| 
