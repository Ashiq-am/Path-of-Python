# Python program explaining
# numpy.char.ljust() method

# importing numpy
import numpy as geek

# input array
in_arr = geek.array(['Numpy', 'Python', 'Pandas'])
print ("Input array : ", in_arr)

# setting the width of each string to 8
width = 8

# output array when fillchar is not passed
out_arr = geek.char.ljust(in_arr, width)
print ("Output left justified array: ", out_arr)
