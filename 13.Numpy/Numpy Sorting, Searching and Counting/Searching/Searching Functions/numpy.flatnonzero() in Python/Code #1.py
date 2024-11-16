# Python program explaining
# flatnonzero() function

import numpy as geek

arr = geek.arange(-3, 4)

print("Input array : ", arr)

out_arr = geek.flatnonzero(arr)
print("Indices of non zero elements : ", out_arr)
