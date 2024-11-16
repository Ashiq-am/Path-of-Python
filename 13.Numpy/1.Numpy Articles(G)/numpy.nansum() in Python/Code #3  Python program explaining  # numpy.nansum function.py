# Python program explaining
# numpy.nansum function

import numpy as geek

in_arr = geek.array([[2, 2, 2], [2, 2, geek.nan]])

print("Input array : ", in_arr)

out_sum = geek.nansum(in_arr, axis=1)
print("sum of array elements taking axis 1: ", out_sum)
