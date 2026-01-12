
''' Sample code to convert a DMS value to DD

Resources:
https://gist.github.com/jeteon/89c41e4081d87b798d8006b16a52c695
https://www.codersarts.com/forum/python-programming-help/convert-dms-to-dd-in-python-codersarts

'''


#Define the function to convert the value:
def dms2dd(DMS_coord):
    dd = float(DMS_coord[0]) + float(DMS_coord[1])/60 + float(DMS_coord[2])/(60*60);
    return dd;

# Create a variable to pass in, then call the function:

#Format the DMS value with commas: -30,30,0

DMS_coord=(53,35,22.2)

print (f"The input DMS value is: {DMS_coord}\n")
DD_value = dms2dd(DMS_coord)

print(f'Its DD form is {DD_value}')



#DMS_coord=tuple(int(x.strip()) for x in input().split(','))