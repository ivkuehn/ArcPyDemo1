# Scripting with ArcPy: Exercise 7 - Describing data
#
# This script demonstrates how a "describe" object is created and used.
 
import arcpy
fc = "V:/ArcPyDemo1/Data/SanDiego/climate.shp"
dsc = arcpy.da.Describe(fc)

print (dsc['OIDFieldName'])
print (dsc['hasSpatialIndex'])

if not dsc['hasSpatialIndex']:
    arcpy.AddSpatialIndex_management(fc)

print(dsc.keys())