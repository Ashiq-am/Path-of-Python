# Python program explaining
# numpy.recarray.any() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([(5.0, 2), (3.0, 4)],
	dtype =[('a', float), ('b', int)])
print ("Input array : ", in_arr)

# convert it to a record array, using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)
print("Record array of float: ", rec_arr.a)

# applying recarray.any methods to float record array
out_arr = geek.recarray.any(rec_arr.a)
print ("Output array: ", out_arr)

print("\nRecord array of int: ", rec_arr.b)
# applying recarray.any methods
# to int record array
out_arr = geek.recarray.any(rec_arr.b)
print ("Output array: ", out_arr)
