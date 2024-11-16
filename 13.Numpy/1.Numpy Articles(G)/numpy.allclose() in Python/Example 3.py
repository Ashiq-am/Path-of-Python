# Python program explaining
# allclose() function

import numpy as geek

# input arrays
in_arr1 = geek.array([5e5, 1e-7, geek.nan])
print ("1st Input array : ", in_arr1)

in_arr2 = geek.array([5e5, 1e-7, geek.nan])
print ("2nd Input array : ", in_arr2)

# setting the absolute and relative tolerance
rtol = 1e-06
atol = 1e-09

res = geek.allclose(in_arr1, in_arr2, rtol, atol)
print ("Are the two arrays are equal within the tolerance: \t", res)
