# Python program explaining
# column_stack() function

import numpy as geek

# input array
in_arr1 = geek.array([[ 1, 2, 3], [ -1, -2, -3]] )
print ("1st Input array : \n", in_arr1)

in_arr2 = geek.array([[ 4, 5, 6], [ -4, -5, -6]] )
print ("2nd Input array : \n", in_arr2)

# Stacking the two arrays
out_arr = geek.column_stack((in_arr1, in_arr2))
print ("Output stacked array :\n ", out_arr)
