# Python program explaining
# numpy.recarray.compress() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([[(5.0, 2), (3.0, -4), (6.0, 9)], [(9.0, 1), (5.0, 4), (-12.0, -7)]],
		dtype =[('a', float), ('b', int)])
print ("Input array : ", in_arr)

# convert it to a record array, using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)
print("Record array of int: ", rec_arr.b)

# applying recarray.compress methods to float record array
float_rec_arr = rec_arr.a
print("Record array of float: ", float_rec_arr)
out_arr = (rec_arr.a).compress([0, 1], axis = 0)
print ("Output compressed array : ", out_arr)

# applying recarray.compress methods to int record array
int_rec_arr = rec_arr.b
print("Record array of int: ", int_rec_arr)
out_arr = int_rec_arr.compress([True, False], axis = 1)
print ("Output compressed array : ", out_arr)
