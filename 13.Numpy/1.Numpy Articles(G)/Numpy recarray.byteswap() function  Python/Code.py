# Python program explaining
# numpy.recarray.byteswap() method

# importing numpy as geek
import numpy as geek

# creating input array with 2 different field
in_arr = geek.array([(5.0, 2), (3.0, -4), (6.0, 9)],
					dtype =[('a', float), ('b', int)])
print ("Input array : ", in_arr)

# convert it to a record array,
# using arr.view(np.recarray)
rec_arr = in_arr.view(geek.recarray)


# applying recarray.byteswap methods to record array
out_arr = rec_arr.byteswap()
print ("Output swapped record array : ", out_arr)
