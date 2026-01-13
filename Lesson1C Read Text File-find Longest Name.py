# Reading values from a text file to find the longest name
#NR 426 Demo Lesson 1c

import os, sys
path = r"C:\Users\Documents\NR426\Lesson 1 - Python Basics"
file = "Student Names.txt"
full = os.path.join(path, file)
print (full)

#Check that the file exists
if not os.path.exists(full):
     print ("file " + full + " doesn't exist")
     print ("Exiting script")
     sys.exit()
# We don't need an else statement here, and that's ok

# Instantiate (create) a variable to hold the length of the longest name
a = 0
# Instantiate a variable to hold the longest name
longestname = ""

# Open the text file of student names in read mode
with open(full, "r") as f:
    names = f.readlines()
    print ("The student names are:")
    for x in names: print (x[0:-1])  # Print out all the student names
    # Loop through each name and get its length. If that name's length is greater than the variable a, then
    # a will take on that value
    for n in names:
        len_n = len(n)
        if len_n > a:
            a = len_n  #This sets the value of a to the length of the current name
            longestname = n[0:-1]   #  This sets the value of longest name to the current name
        #print (n[0:-1] + ": " +str(len(n)))
# Alternatively use the max function with key=len

print ("The person with the longest name is {0}".format(longestname))

