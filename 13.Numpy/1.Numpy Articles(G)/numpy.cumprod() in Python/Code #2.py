# Python program explaining
# numpy.cumprod() function

import numpy as geek

in_arr = geek.array([[2, 4, 6], [1, 3, 5]])

print("Input array : ", in_arr)

out_prod = geek.cumprod(in_arr)
print("cumulative product of array elements: ", out_prod)
