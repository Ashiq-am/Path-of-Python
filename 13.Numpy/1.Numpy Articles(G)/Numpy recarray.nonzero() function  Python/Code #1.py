# Python program explaining
# numpy.recarray.nonzero() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([[(0.0, 2), (3.0, -4), (0.0, 9)],
					[(9.0, 1), (5.0, 0), (-12.0, -7)]],
					dtype =[('a', float), ('b', int)])

print ("Input array : ", in_arr)

# convert it to a record array,
# using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)
print("Record array of float: ", rec_arr.a)
print("Record array of int: ", rec_arr.b)

# applying recarray.nonzero methods
# to float record array
out_arr = rec_arr.a.nonzero()
print ("Indices of non zero elements : ", out_arr)

# applying recarray.nonzero methods
# to int record array
out_arr = rec_arr.b.nonzero()
print ("Indices of non zero elements : ", out_arr)
