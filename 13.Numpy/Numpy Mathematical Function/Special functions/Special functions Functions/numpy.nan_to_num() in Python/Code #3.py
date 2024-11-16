# Python program explaining
# numpy.nan_to_num function

import numpy as geek

in_arr = geek.array([[2, 2, 2], [2, 2, 6]])

print("Input array : ", in_arr)

out_arr = geek.nan_to_num(in_arr)
print("Output array: ", out_arr)
