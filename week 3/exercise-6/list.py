# Python file for exercise 6 - list.py
## Carter Hanford

# import libraries
import arcpy
from arcpy import env

# import workspace
arcpy.env.workspace = r"C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\week 3\data\Exercise06"

# create list
fclist = arcpy.ListFeatureClasses()
print (fclist)


