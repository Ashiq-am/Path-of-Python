# Python program explaining
# numpy.char.greater() method

# importing numpy
import numpy as geek

# input arrays
in_arr1 = geek.array(['10', '11', '122', '15'])
print ("1st Input array : ", in_arr1)

in_arr2 = geek.array(['10', '13', '121', '14'])
print ("2nd Input array : ", in_arr2)


# checking if in_arr1 > in_arr2
out_arr = geek.char.greater(in_arr1, in_arr2)
print ("Output array: ", out_arr)
