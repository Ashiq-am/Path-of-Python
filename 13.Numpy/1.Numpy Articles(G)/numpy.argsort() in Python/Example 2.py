# Python program explaining
# argpartition() function

import numpy as geek

# input 2d array
in_arr = geek.array([[ 2, 0, 1], [ 5, 4, 3]])
print ("Input array : ", in_arr)

# output sorted array indices
out_arr1 = geek.argsort(in_arr, kind ='mergesort', axis = 0)
print ("Output sorteded array indices along axis 0: ", out_arr1)
out_arr2 = geek.argsort(in_arr, kind ='heapsort', axis = 1)
print ("Output sorteded array indices along axis 1: ", out_arr2)
