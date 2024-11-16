# Python program explaining
# numpy.char.less_equal() method

# importing numpy
import numpy as geek

# input arrays
in_arr1 = geek.array(['Geeks', 'for', 'Geek', 'Numpy'])
print ("1st Input array : ", in_arr1)
in_arr2 = geek.array(['Geek', 'for', 'Geek', 'numpy'])
print ("2nd Input array : ", in_arr2)

# checking if in_arr1 <= in_arr2
out_arr = geek.char.less_equal(in_arr1, in_arr2)
print ("Output array: ", out_arr)
