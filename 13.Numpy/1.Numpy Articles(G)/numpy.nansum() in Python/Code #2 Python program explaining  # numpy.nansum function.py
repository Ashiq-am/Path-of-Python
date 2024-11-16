# Python program explaining
# numpy.nansum function

import numpy as geek

in_arr = geek.array([[2, 2, 2], [2, 2, geek.nan]])

print("Input array : ", in_arr)

out_sum = geek.nansum(in_arr)
print("sum of array elements: ", out_sum)
