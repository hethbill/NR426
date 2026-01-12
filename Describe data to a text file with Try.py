# This script describes an input feature class and writes some properties
# out to a text file
# It also makes use of simple error handling with a Try -Except statement

## Be sure to set the variables below before trying to run!

# Import the arcpy module
import arcpy
## ******************************** ##
# Set some variables #  C H A N G E   T H E S E :
txtfile = r"C:\Users\MapGirl\Documents\NR426-427\describing.txt"       # Full path to txt file you want to create
arcpy.env.workspace = r"C:\Data\Beth_Data"  # Full path to workspace
data = "NorthwestRoadTrip.gdb"              # Name only of data to describe
## ******************************** ##
# Create and open output text file
outFile = open(txtfile, "w")

# Describe the data
dsc = arcpy.Describe(data)

#Write information out to the text file
outFile.write("***** Describe information for "+data+" *****\n\n")       
try:
    outFile.write(data+ " has " +dsc.shapetype+ " geometry\n")
except:
    outFile.write(data+ " is a "+dsc.datatype+" and has no shapetype\n")
outFile.write("The full path is " + dsc.catalogpath+ "\n")

# Close files
outFile.close()

print ("Finished")