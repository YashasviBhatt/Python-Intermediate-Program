# using numpy slicing

import numpy as np          # numpy is used to implement mathematical tools and equation

x=[[1,2,3],[4,5,6],[7,8,9]]
print("1 ",x)
print("2 ",type(x))
#converting Multi-Dimensional List into Numpy ND Array
print("3 ",np.array(x))
z=np.array(x)
print("4 ",z)
#printing first row
print("5 ",z[0:1])
#printing first 2 rows
print("6 ",z[0:2])
#printing first 3 rows
print("7 ",z[0:3])
#printing from 1st row to last row and last column [6,9]
print("8 ",z[1:,2])
#printing from 1st row to last row and first column [4,7]
print("9 ",z[1:,0])
#printing 1st row last column [3]
print("10 ",z[0:1,2])
#printing 1st column and last column
print("11 ",z[0:,(0,2)])
#printing first row
print("12 ",z[0:,0])
#printing middle row
print("13 ",z[0:,1])
#printing last row
print("14 ",z[0:,2])
#printing first row middle comumn
print("15 ",z[0,1:2])
#printing the datatype of z
print("16 ",type(z))
#printing column 1 and column 3
print("17 ",z[:,(0,2)])
#printing first column first and last row
print("18 ",z[[(0,2)],0])
#printing middle column first and last row
print("19 ",z[[(0,2)],1])
#printing last column first and last row
print("20 ",z[[(0,2)],2])
#printing first row first and last column
print("21 ",z[0,(0,2)])
#printing second row first and last column
print("22 ",z[1,(0,2)])
#printing last row first and last column
print("23 ",z[2,(0,2)])