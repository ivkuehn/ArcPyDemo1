import arcpy

#Set variable names to the 4 user inputs
className = arcpy.GetParameterAsText(0)
distance = arcpy.GetParameterAsText(1)
A = arcpy.GetParameterAsText(2)
B = arcpy.GetParameterAsText(3)

#Message results back to the status window when run
arcpy.AddMessage(f"The class name is {className}.")
arcpy.AddWarning(f"The distance is {distance}.")
arcpy.AddError(f"{A} + {B} = {A+B}?!")