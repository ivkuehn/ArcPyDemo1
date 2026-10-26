#Scripting with ArcPy: Exercise 8 - Using cursors and the geometry object
#
# This script demonstrates how cursors are used to
#  process records in an attribute table, on at a time

import arcpy

# Specify the feature class, raster, or table to examine
fc = "V:\\ArcPyDemo1\\Data\\SanDiego\\climate.shp"

# Create a cursor (this is like opening a file)
rows = arcpy.da.SearchCursor(fc,['Climate_ID','Zone'])

# Use a For loop to iterate through all rows
for row in rows:
    climateVal = row[0]
    zoneVal = row[1]
    # Print the values for the fields we specified
    print('The climate is {} and the zone is {}'.format(climateVal,zoneVal))