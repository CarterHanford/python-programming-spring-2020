import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)
out_file = arcpy.GetParameterAsText(1)

#r'C:\Users\hanfordca\Documents\GitHub\python-programming-spring-2020\project 1\data\tlgdb_2019_a_us_school.gdb'

feature_list = arcpy.ListFeatureClasses()

f = open(out_file, 'w')
header = f.write('Feature Class, Feature Count, Projection, Shape \n')

for feature in feature_list:
    feature_count = arcpy.GetCount_management(feature)
    desc = arcpy.Describe(feature)
    projection = desc.SpatialReference.name
    shape_type = desc.shapeType
    seperator = ", "
    #print(feature + seperator, str(feature_count) + seperator, projection + seperator, shape_type)
    f.write(feature + seperator + str(feature_count) + seperator + projection + seperator + shape_type + '\n')

f.close()