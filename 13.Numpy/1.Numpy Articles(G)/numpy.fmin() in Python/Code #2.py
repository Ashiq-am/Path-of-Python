# Python program explaining
# fmin() function

import numpy as geek

in_arr1 = [2, 8, 125, geek.nan]
in_arr2 = [geek.nan, 3, 115, geek.nan]

print("Input array1 : ", in_arr1)
print("Input array2 : ", in_arr2)

out_arr = geek.fmin(in_arr1, in_arr2)
print("Output array : ", out_arr)
