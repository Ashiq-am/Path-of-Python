# Python program explaining
# numpy.nancumprod() function

import numpy as geek

in_arr = geek.array([[2, 2, 2], [2, 2, geek.nan]])

print("Input array : ", in_arr)

out_prod = geek.nancumprod(in_arr)
print("cumulative product of array elements: ", out_prod)
