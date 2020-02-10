# Challenge Problem 2 - Exercise 6
## Carter Hanford

# This challenge problem asks us to write a script that reads all feature classes in the OSM.gdb
# and copy only the polygon feature classes to a new file geodatabase

# import directories
import arcpy
from arcpy import env
env.overwriteOutput = True

# create workspace environment and create new directory for GDB
arcpy.env.workspace = r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\OSM.gdb"
arcpy.CreateFileGDB_management(r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\Results", "challenge2.gdb")

# let's create a list so we can reference it later
fclist = arcpy.ListFeatureClasses()
print(fclist)

# now we will create the for loop that sends only the polygon feature classes to our new geodatabase
# i used "endswith" to indicate which feature classes to send to the new geodatabase
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    if 'fclist'.endswith('polygon'):
        arcpy.CopyFeatures_management(fc, r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\Results\challenge2.gdb")