# Python program explaining
# numpy.recarray.argmin() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([[(5.0, 2), (3.0, 4), (6.0, 9)],
					[(9.0, 1), (5.0, 4), (-12.0, -7)]],
					dtype =[('a', float), ('b', int)])
print ("Input array : ", in_arr)

# convert it to a record array,
# using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)
print("Record array of float: ", rec_arr.a)
print("Record array of int: ", rec_arr.b)

# applying recarray.argmin methods to
# float record array along axis 1
out_arr = geek.recarray.argmin(rec_arr.a, axis = 1)
print ("Output array along axis 1: ", out_arr)

# applying recarray.argmin methods to
# int record array along axis 0
out_arr = geek.recarray.argmin(rec_arr.b, axis = 0)
print ("Output array along axis 0: ", out_arr)
