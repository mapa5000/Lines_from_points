'''
***///*** === Lines_from_points === ***///*** 

This tool creates stubs (lines) from points in a pipeline system in ArcMAP
Geographic Coordinate System: GCS_North_American_1983
Datum: D_North_American_1983
Prime Meridian: Greenwich Angular
Unit: Degree
'''


# Marco Portillo
# For Celerety Consulting Group

# Import system modules

import arcpy
from arcpy import env

# Set local variables
input_table = r"C:\Users\Marco\Desktop\stub_1_3.csv"
out_lines = r"C:\Users\Marco\Desktop\Parcelas Fresno.gdb\stub_1_3"

#XY To Line
arcpy.XYToLine_management(input_table,out_lines,
                         "start_x","start_y","end_x","end_y","GEODESIC")

# Set local variables
input_table = r"C:\Users\Marco\Desktop\stub_3_6L.csv"
out_lines = r"C:\Users\Marco\Desktop\Parcelas Fresno.gdb\stub_3_6L"
#XY To Line
arcpy.XYToLine_management(input_table,out_lines,
                         "start_x","start_y","end_x","end_y","GEODESIC")

# Set local variables
input_table = r"C:\Users\Marco\Desktop\stub_3_6R.csv"
out_lines = r"C:\Users\Marco\Desktop\Parcelas Fresno.gdb\stub_3_6R"
#XY To Line
arcpy.XYToLine_management(input_table,out_lines,
                         "start_x","start_y","end_x","end_y","GEODESIC")


# Set local variables
input_table = r"C:\Users\Marco\Desktop\stub_6L_7L.csv"
out_lines = r"C:\Users\Marco\Desktop\Parcelas Fresno.gdb\stub_6L_7L"
#XY To Line
arcpy.XYToLine_management(input_table,out_lines,
                         "start_x","start_y","end_x","end_y","GEODESIC")

# Set local variables
input_table = r"C:\Users\Marco\Desktop\stub_6R_7R.csv"
out_lines = r"C:\Users\Marco\Desktop\Parcelas Fresno.gdb\stub_6R_7R"
#XY To Line
arcpy.XYToLine_management(input_table,out_lines,
                         "start_x","start_y","end_x","end_y","GEODESIC")

print "***///Script Finalizado///***"
print "***/////Check results/////***"
