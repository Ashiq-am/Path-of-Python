# Python program explaining
# numpy.nanprod function

import numpy as geek

in_arr = geek.array([[2, 2, 2], [2, 2, geek.nan]])

print("Input array : ", in_arr)

out_prod = geek.nanprod(in_arr, axis=1)
print("product of array elements taking axis 1: ", out_prod)
