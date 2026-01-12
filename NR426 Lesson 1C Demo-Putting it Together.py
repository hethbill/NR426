'''
NR426 Lesson 1C -  Putting it all together
This script will show use of Python basics including creating variables, importing modules,
lists and loops, if statements, and user input.

Written by instructor Elizabeth Tulanowski
Aug 2020

Purpose: To work with fictional stream data and calculate and average flow for a given year
'''
print ("Beginning 1C Demo script.........")

# Import necessary modules

# Create variables
year = 2015
print ("\nThe selected year is " + str(year))   #That \n makes an empty line

site = "Fall Creek"
print ("The selected site is: " + site)
print()  #Just makes an empty line

#Fictional precip values, these could be what you read in from a table or text file
data15 = [1.2, 1.1, 0.8]
data18 = [0.9, 2.1, 1.8]

print ("Working on the average precip values section....\n")
if site == "Fall Creek":
    if year == 2015:
        avg15 = sum(data15) / len(data15)
        print("The precipitation measurements for " + str(year) + " are:")
        for y in data15:
            print ("\t"+str(y))       # \t makes a tab, to indent the output for readability
        print ("The mean precipitation value is " + str(round(avg15,3)))
    elif year == 2018:
        avg18 = sum(data18) / len(data18)
        print("The precipitation measurements for " + str(year)) + " are:"
        for y in data18:
            print (y)
    else:
        print ("We don't have that data")
else:
    print ("This is not the site you are looking for")

#Reference for calculating average value in a list
# https://www.geeksforgeeks.org/find-average-list-python/


##  What if you had a 4-digit year and you need a 2-digit year?
yr2 = str(year)[-2:]
print ("The 2-digit year is: " + str(yr2))
print ()

print ("Working on the years to calculate section....")
# Maybe we have a list of years
yrs = [2009, 2011, 2014, 2015, 2018]
yrs2calc= []
for yr in yrs:
    if yr < 2010:
        print ("Year is {0}: ".format(yr) + "We're not dealing with data that old")
    elif yr > 2010 and yr < 2015:
        yrs2calc.append(yr)
        print ("Create a query to find rows with Year = {0}, then do calculations on it".format(yr))
    elif yr > 2015:
        print ("Year {0}: This is the newer data to work with".format(yr))
    else:
        print ("Can't determine year")
print ("\nThe list of years to calculate is:")
print (yrs2calc)
print ()

# Other evaluation conditions:
if not year:
    print ("Year has no value")
elif year != 2015:
    print ("Year does not equal 2015")
