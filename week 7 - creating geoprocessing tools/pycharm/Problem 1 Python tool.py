import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)
#r'C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\project 1\data\imagery'

raster_list = arcpy.ListRasters()
arcpy.AddMessage("There are " + str(len(raster_list)) + " rasters in the folder.")

for raster in raster_list:
    desc = arcpy.Describe(raster)
    arcpy.AddMessage("Raster Name: " + raster)
    arcpy.AddMessage("Band Count:       %d" % desc.bandCount)
    arcpy.AddMessage("Compression Type: %s" % desc.compressionType)
    arcpy.AddMessage("Raster Format:    %s" % desc.format)
    arcpy.AddMessage("Spatial Reference: %s" % desc.SpatialReference.name)