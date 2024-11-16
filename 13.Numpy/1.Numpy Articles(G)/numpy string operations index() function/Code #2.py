# Python program explaining
# numpy.char.index() method

# importing numpy
import numpy as geek

# input arrays
in_arr = geek.array(['aAaAaA', 'aA', 'abBABba'])
print ("Input array : ", in_arr)

# output arrays
out_arr = geek.char.index(in_arr, sub ='A', start = 1, end = 4)
print ("Output array: ", out_arr)
