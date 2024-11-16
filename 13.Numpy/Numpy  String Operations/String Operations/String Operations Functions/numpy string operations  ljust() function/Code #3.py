# Python program explaining
# numpy.char.ljust() method

# importing numpy
import numpy as geek

# input array
in_arr = geek.array(['1', '11', '111'])
print ("Input array : ", in_arr)

# setting the width of each string to 5
width = 5

# output array
out_arr = geek.char.ljust(in_arr, width, fillchar ='-')
print ("Output left justified array: ", out_arr)
