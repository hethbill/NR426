# NR426 Lesson 1A Putting It Together Demo Script
# Written by Elizabeth Tulanowski

# pseudocode

#Import modules
import os, math

#Set up variables
path1 = "C:\data\Colorado"
path2 =  "C:\Data\Colorado\LarimerCo"
path3 =  "C:\\Data\\Colorado\\LarimerCo"
path4 =  "C:/Data/Colorado/LarimerCo"

path =  r"C:\Data\Colorado\LarimerCo"
shp = "FC_boundarynew.shp"
fieldname = "Area"
acres = 10

#Convert values from acres to sq miles
sqmi = acres / 640
print (sqmi)
print ("The area in sqmi is " + str(sqmi))
print ("Miles = " + str(mi))

# Parse out the pieces of the file name we need
print (shp[:5])
print(shp[-4:])
print (shp[:-4])

# Combine the path with the file name
fullpath = os.path.join(path, shp)
print (fullpath)

# Return the length of the string
print ("The length of the pathname is: " + str(len(path)))
len(fullpath)



#Combine our final results into a nice sentence
# f-string
print(f"The full path to the data is: {fullpath} and has {len(fullpath)} characters")


#Math module
#import math
from math import *
#math.sqrt(sqmi)
sqrt(sqmi)
