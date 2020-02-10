# coding: utf-8
import arcpy
from arcpy import env
env.workspace = r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\Exercise06"
shape_exists = arcpy.Exists("cities.shp")
print (shape_exists)
# True
import arcpy
from arcpy import env
env.workspace = r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\Exercise06"
if arcpy.Exists("cities.shp"):
    arcpy.CopyFeatures_management("cities.shp", "results/cities_copy.shp")