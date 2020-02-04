# coding: utf-8
import arcpy
arcpy.GetInstallInfo()
# {'LicenseLevel': 'Advanced', 'InstallDir': 'c:\\program files\\arcgis\\pro\\', 'Installer': 'wurthrs', 'ProductName': 'ArcGISPro', 'Version': '2.3', 'SourceDir': 'U:\\Lab 204\\ArcGIS_Pro_2.3\\ArcGISPro\\', 'InstallType': 'N/A', 'BuildNumber': '15769', 'InstallDate': '3/7/2019', 'InstallTime': '13:33:55', 'SPNumber': 'N/A', 'SPBuild': 'N/A'}
print ("hello world")
# hello world
arcpy.GetCount_management('County')
# <Result '115'>
arcpy.MakeFeatureLayer_management("C:\\Users\\hanfordca\\Documents\\GitHub\\python-programming-spring-2020\\Week 2\\data\\Missouri.gdb\\Roads", "carters_county_layer")
# <Result 'carters_county_layer'>
arcpy.CopyFeatures_management('County', "Lincoln_County")
# <Result 'C:\\Users\\hanfordca\\Documents\\GitHub\\python-programming-spring-2020\\Week 2\\Week 2 Lecture 1\\Week 2 Lecture 1.gdb\\Lincoln_County'>
arcpy.Clip_analysis('carters_county_layer', 'Lincoln_County', 'Lincoln_County_Roads')
# <Result 'C:\\Users\\hanfordca\\Documents\\GitHub\\python-programming-spring-2020\\Week 2\\Week 2 Lecture 1\\Week 2 Lecture 1.gdb\\Lincoln_County_Roads'>