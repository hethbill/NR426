#Sample code to demonstrate how a basic function works

# Dance steps: The Hokey Pokey
def HokeyPokey (part):
    print (f"Put your {part} in")
    print(f"Put your {part} out")
    print(f"Put your {part} in")
    print(f"And you shake it all about")
    print ("You do the Hokey Pokey and you turn yourself around")
    print ("That's what it's all about\n")

# Run the function on one body part:
HokeyPokey("pinky")

print ()

#Run the function on a list of body parts:
parts = ["left foot", "right foot", "left arm", "right arm"]
for p in parts:
    HokeyPokey(p)

print ()

print ("Now I'm tired!")

# # # # # #

# ## How does this relate to geospatial?
#
# # Function to check for data existence
# import os, sys
# path = r"C:\Data\Beth_Dat"
# def CheckData(inputdata):
#     if os.path.exists(inputdata):
#         msg = "first dataset is there"
#         return(msg)
#     else:
#         msg = "Printing else, and quitting"
#         return (msg)
#         sys.exit()
#
# print (CheckData(path))
#
# print ("done")

# # # # # #

# ## working with values
# def conv_avg(nums):
#     #Enter a list of elevations in meters, and it will average them and convert to feet
#     total = (nums)
#     avg = total / (len(nums))
#     avg_ft = avg / .3048
#     return (avg_ft)
#
# result = conv_avg([3000, 4000, 3500, 1000, 2789])
# print (f"The average elevation in feet is {round(result,2)}")
