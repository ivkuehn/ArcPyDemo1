# Name: Select_Example2.py
# Description: Select roads of Class 4 from major roads tin the gnatcatcher habitat study area
   
# Import system modules
import arcpy
   
# Set workspace
arcpy.env.workspace = "V:/ArcPyDemo1/Data/SanDiego"
   
# Set local variables
in_features = "majorrds.shp"
out_feature_class = "V:/ArcPyDemo1/Scratch/majorrdsClass4.shp"
where_clause = '"CLASS" = \'4\''
   
# Execute Select
arcpy.Select_analysis(in_features, out_feature_class, where_clause)

buffRoads = "V:/ArcPyDemo1/Scratch/BufferedRoads.shp"
buffDist = "500 meters"
arcpy.Buffer_analysis(out_feature_class,buffRoads,buffDist,'','','ALL')

#%% Exercise 2
arcpy.Exists("climate.shp")

myFields = arcpy.ListFields("climate.shp")
myField = myFields[0]

#%% Exercise 3
myPoint = arcpy.Point()

myPoint.X = 6266956
myPoint.Y = 1876781
myPoint.ID = 1

myPoly = arcpy.SearchCursor("V:\\ArcPyDemo1\\data\\SanDiego\\study_quads.shp").next().Shape
print (myPoint.within(myPoly))

#%% Exercise 4

arcpy.env.workspace = "V:/ArcPyDemo1/Data/SanDiego"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")
arcpy.env.overwriteOutput = True

# Set local variables
in_features = "majorrds.shp"
out_feature_class = "majorrdsClass4.shp"
where_clause = '"CLASS" = \'4\''
  
# Execute Select
arcpy.Select_analysis(in_features, out_feature_class, where_clause)

