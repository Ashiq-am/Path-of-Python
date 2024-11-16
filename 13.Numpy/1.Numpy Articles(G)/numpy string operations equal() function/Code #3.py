# Python program explaining
# numpy.char.equal() method

# importing numpy
import numpy as geek

# input arrays
in_arr1 = geek.array(['10', '11', '12'])
print ("1st Input array : ", in_arr1)

in_arr2 = geek.array(['10', '11', '121'])
print ("2nd Input array : ", in_arr2)


# checking if they are equal
out_arr = geek.char.equal(in_arr1, in_arr2)
print ("Output array: ", out_arr)
