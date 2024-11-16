# Python program explaining
# numpy.recarray.dot() method

# importing numpy as geek
import numpy as geek

# creating 2 input array with 2 different field
in_arr1 = geek.array([[(5.0, 2), (3.0, -4), (6.0, 9)],
					[(9.0, 1), (5.0, 4), (-12.0, -7)]],
					dtype =[('a', float), ('b', int)])

in_arr2 = geek.array([[(2.0, 1), (4.0, -3)],
					[(8.0, 3), (6.0, 5)],
					[(6.0, -5), (-5.0, 4)]],
					dtype =[('a', float), ('b', int)])

print ("1st Input array : ", in_arr1)
print ("2nd Input array : ", in_arr2)

# convert it to a record array,
# using arr.view(np.recarray)
rec_arr1 = in_arr1.view(geek.recarray)
print("1st Record array of float: ", rec_arr1.a)
print("1st Record array of int: ", rec_arr1.b)
rec_arr2 = in_arr2.view(geek.recarray)
print("2nd Record array of float: ", rec_arr2.a)
print("2nd Record array of int: ", rec_arr2.b)

# applying recarray.dot methods
# between two float record array
out_arr1 = rec_arr1.a.dot( rec_arr2.a)
print ("Output float array : ", out_arr1)

# applying recarray.dot methods
# between two int record array
out_arr1 = rec_arr1.b.dot( rec_arr2.b)
print ("Output int array : ", out_arr1)
