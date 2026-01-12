'''
Header code:
NR426 - Programming for GIS 1
Lesson 1B Demo - Putting it Together - Lists and Loops

Written by Instructor Elizabeth Tulanowski, Aug 2020
'''
print ("Starting List script\n")
# Import any needed libraries
import os

# Declare variables
# City to add to list
FC = "Fort Collins"
# City  to remove from list
LV = "Loveland"

# Create a list of cities
cities = ["Wellington", "Greeley", "Loveland", "Longmont", "Boulder"]

# print ("Printing just the list:")
# print (cities)
#
# # Print out a well formatted list, sequentially numbered
# cities.append(FC)
# cities.remove(LV)
#
# print ("Printing it nicer:")
# counter = 1
# for eachitem in cities:
#     print ("City name {0}: ".format(counter) +  eachitem)
#     counter = counter + 1
#


# Create a new variable for an address  - Street, City, State
addr = "101 S. College Ave, Fort Collins, CO"

#Use split to parse out just the city name
add_list = addr.split(", ")

print (add_list)
StreetAddr = add_list[0]
print (StreetAddr)

print (add_list[1])

print ("\n  - - - List script completed - - - ")
