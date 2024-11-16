# Python program explaining
# numpy.recarray.max() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([[(5.0, 2), (3.0, -4), (6.0, 8)],
					[(9.0, 1), (5.0, 4), (-12.0, -7)]],
					dtype =[('a', float), ('b', int)])

print ("Input array : ", in_arr)

# convert it to a record array,
# using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)
print("Record array of float: ", rec_arr.a)
print("Record array of int: ", rec_arr.b)

# applying recarray.max methods
# to float record array along default axis
# i, e along flattened array
out_arr1 = rec_arr.a.max()
# Maximum of the flattened array
print("\nMax of float record array, axis = None : ", out_arr1)


# applying recarray.max methods
# to float record array along axis 0
# i, e along vertical
out_arr2 = rec_arr.a.max(axis = 0)
# Maximum along 0 axis
print("\nMax of float record array, axis = 0 : ", out_arr2)


# applying recarray.max methods
# to float record array along axis 1
# i, e along horizontal
out_arr3 = rec_arr.a.max(axis = 1)
# Maximum along 0 axis
print("\nMax of float record array, axis = 1 : ", out_arr3)


# applying recarray.max methods
# to int record array along default axis
# i, e along flattened array
out_arr4 = rec_arr.b.max()
# Maximum of the flattened array
print("\nMax of int record array, axis = None : ", out_arr4)


# applying recarray.max methods
# to int record array along axis 0
# i, e along vertical
out_arr5 = rec_arr.b.max(axis = 0)
# Maximum along 0 axis
print("\nMax of int record array, axis = 0 : ", out_arr5)


# applying recarray.max methods
# to int record array along axis 1
# i, e along horizontal
out_arr6 = rec_arr.b.max(axis = 1)
# Maximum along 0 axis
print("\nMax of int record array, axis = 1 : ", out_arr6)
