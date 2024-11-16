# Python program explaining
# allclose() function

import numpy as geek

# input arrays
in_arr1 = geek.array([5e5, 1e-7, 4.000004e6])
print ("1st Input array : ", in_arr1)

in_arr2 = geek.array([5.00001e5, 1e-7, 4e6])
print ("2nd Input array : ", in_arr2)

# setting the absolute and relative tolerance
rtol = 1e-05
atol = 1e-08

res = geek.allclose(in_arr1, in_arr2, rtol, atol)
print ("Are the two arrays are equal within the tolerance: \t", res)
