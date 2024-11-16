# Python program explaining
# numpy.nanprod function

import numpy as geek

in_arr = geek.array([[2, 2, 2], [2, 2, geek.nan]])

print("Input array : ", in_arr)

out_prod = geek.nanprod(in_arr)
print("product of array elements: ", out_prod)
