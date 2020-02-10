import arcpy
from arcpy import env

env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\Exercise06"
fieldlist = arcpy.ListFields("cities.shp")

for field in fieldlist:
    print (field.name + " " + field.type)