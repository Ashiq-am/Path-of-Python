# Python program explaining
# searchsorted() function

import numpy as geek

# input array
in_arr = [2, 3, 4, 5, 6]
print("Input array : ", in_arr)

# the number which we want to insert
num = 4
print("The number which we want to insert : ", num)

out_ind = geek.searchsorted(in_arr, num)
print("Output indices to maintain sorted array : ", out_ind)
