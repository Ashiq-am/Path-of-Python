# Python program explaining
# numpy.char.rjust() method

# importing numpy
import numpy as geek

# input array
in_arr = geek.array(['Numpy', 'Python', 'Pandas'])
print ("Input array : ", in_arr)

# setting the width of each string to 8
width = 8

# output array when fillchar is not passed
out_arr = geek.char.rjust(in_arr, width)
print ("Output right justified array: ", out_arr)
