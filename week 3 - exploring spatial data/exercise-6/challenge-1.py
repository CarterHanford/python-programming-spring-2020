# Challenge Problem 1 - Exercise 6
## Carter Hanford

# Let's create a script that reads all of the feature classes in a workspace and then prints
# the name of the feature class, plus the geometry.

# import directories
import arcpy

# set workspace
arcpy.env.workspace = r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\OSM.gdb"

# we want the script to list items in a feature class, so we need a list first
fclist = arcpy.ListFeatureClasses()

# now we will create the for loop which identifies the file in our workspace and lists its geometry
# following the same syntax as challenge 1
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print(fcdescribe.name + " is a " + fcdescribe.dataType + " :)")


