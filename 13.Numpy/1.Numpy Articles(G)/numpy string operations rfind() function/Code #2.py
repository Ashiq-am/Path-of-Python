# Python program explaining
# numpy.char.rfind() method

# importing numpy as geek
import numpy as geek

# input arrays
in_arr = geek.array(['aAaAaA', 'aA', 'abBABba'])
print ("Input array : ", in_arr)

# output arrays
out_arr = geek.char.rfind(in_arr, sub ='a', start = 3, end = 7)
print ("Output array: ", out_arr)
