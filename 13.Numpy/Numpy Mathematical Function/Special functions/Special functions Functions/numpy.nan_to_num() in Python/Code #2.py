# Python program explaining
# numpy.nan_to_num function

import numpy as geek

in_arr = geek.array([[2, geek.inf, 2], [2, 2, geek.nan]])

print("Input array : ", in_arr)

out_arr = geek.nan_to_num(in_arr)
print("output array: ", out_arr)
