#Exercise 9 - Geometry objects

#Import arcpy
import arcpy

#Create a variable pointing to the feature class
fc = "V:\\ArcPyDemo1\\Data\\SanDiego\\climate.shp"

#Create a search cursor
rows = arcpy.da.SearchCursor(fc,['Shape@'])

#Get the first row
row = rows.next()

#Get the shape object
feature = row[0]

#Delete the cursor
del rows

#Create a point object and see if it falls in the shape
myPoint = arcpy.Point(X=6283500,Y=1896150)
print(feature.contains(myPoint))