# Python program explaining
# numpy.char.rjust() method

# importing numpy
import numpy as geek

# input array
in_arr = geek.array(['1', '11', '111'])
print ("Input array : ", in_arr)

# setting the width of each string to 5
width = 5

# output array
out_arr = geek.char.rjust(in_arr, width, fillchar ='-')
print ("Output right justified array: ", out_arr)
