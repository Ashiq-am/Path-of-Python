# Python program explaining
# numpy.packbits() function

# importing numpy
import numpy as geek

# creating input array using
# array function
in_arr = geek.array([[[0, 0, 1],
					[1, 1, 0]],
					[[1, 0, 0],
						[1, 1, 1]]])
print ("Input array : ", in_arr)

# packing elements of an array
# using packbits() function
out_arr = geek.packbits(in_arr, axis = 1)

print ("Output packed array along axis 1 : ", out_arr)
