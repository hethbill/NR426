''' Sample code to convert a DMS value to DD

Resources:
https://gist.github.com/jeteon/89c41e4081d87b798d8006b16a52c695
https://www.codersarts.com/forum/python-programming-help/convert-dms-to-dd-in-python-codersarts

'''



def dms2dd(DMS_coord):
    dd = float(DMS_coord[0]) + float(DMS_coord[1])/60 + float(DMS_coord[2])/(60*60);
    return dd;

def dd2dms(DD_coord):
    d = int(DD_coord)
    md = abs(DD_coord - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]

#tup1=(-30,30,0)
print('Please enter a latitude or longitude value in D,M,S')
DMS_coord=tuple(int(x.strip()) for x in input().split(','))
lat = dms2dd(DMS_coord)
print('The input value is in DMS form')
print(f'Its DD form is {lat}')

input1=input('Please enter a latitude or longitude value in DD')
print('The input value is in DD form')
print(f'Its DMS form is {dd2dms(input1)}')
