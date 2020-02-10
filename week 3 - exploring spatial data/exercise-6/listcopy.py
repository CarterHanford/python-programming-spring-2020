# Python file for exercise 6 - listcopy.py
## Carter Hanford

# import libraries
import arcpy
from arcpy import env

# create directory
arcpy.env.workspace = r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\Exercise06"
fclist = arcpy.ListFeatureClasses()

# for loop
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print ("Name: " + fcdescribe.name)
    print ("Data type: " + fcdescribe.dataType)

# script modification
import arcpy
from arcpy import env

arcpy.env.workspace = "C:/EsriPress/Python/Data/Exercise06"
fclist = arcpy.ListFeatureClasses()

for fc in fclist:
    arcpy.CopyFeatures_management(fc, r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\Exercise06" + fc)

# script modification
import arcpy
from arcpy import env
env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\Exercise06"
arcpy.CreateFileGDB_management(r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\Exercise06\Results", "NM.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\Exercise06\Results\NM.gdb\" + fcdesc.basename)"