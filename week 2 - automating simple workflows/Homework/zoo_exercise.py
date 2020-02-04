# coding: utf-8
fcList = ["FieldSightings_Lola", "FieldSightings_Jimmy"]
print(fclist)
# ['FieldSightings_Jimmy', 'FieldSightings_Lola']
print(fcList)
# ['FieldSightings_Lola', 'FieldSightings_Jimmy']
buffList = []
for fc in fcList:
    buff = arcpy.Buffer_analysis(fc,fc+"_Buffer","1 kilometer")
    buffList.append(buff)
for buff in buffList:
    arcpy.SelectLayerByLocation_management('Redlands_Schools', 'WITHIN',buff,0,'ADD_TO_SELECTION')
# <Result 'Redlands_Schools'>
# <Result 'Redlands_Schools'>