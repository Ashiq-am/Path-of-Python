# Python program explaining
# numpy.recarray.swapaxes() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([[(5.0, 2), (3.0, 4), (6.0, -7)],
					[(9.0, 1), (6.0, 4), (-2.0, -7)]],
					dtype =[('a', float), ('b', int)])

print ("Input array : ", in_arr)

# convert it to a record array,
# using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)

# applying recarray.swapaxes methods to
# record array taking axis1 = 0 and axis2 = 1
out_arr = rec_arr.swapaxes(1, 0)

print ("Output record array : ", out_arr)
