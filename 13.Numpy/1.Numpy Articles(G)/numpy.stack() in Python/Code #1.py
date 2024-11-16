# Python program explaining
# stack() function

import numpy as geek

# input array
in_arr1 = geek.array([ 1, 2, 3] )
print ("1st Input array : \n", in_arr1)

in_arr2 = geek.array([ 4, 5, 6] )
print ("2nd Input array : \n", in_arr2)

# Stacking the two arrays along axis 0
out_arr1 = geek.stack((in_arr1, in_arr2), axis = 0)
print ("Output stacked array along axis 0:\n ", out_arr1)

# Stacking the two arrays along axis 1
out_arr2 = geek.stack((in_arr1, in_arr2), axis = 1)
print ("Output stacked array along axis 1:\n ", out_arr2)
