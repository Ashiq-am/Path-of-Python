# Python program explaining
# argpartition() function

import numpy as geek

# input array
in_arr = geek.array([[ 2, 0, 1], [ 5, 4, 9] ])
print ("Input array : \n", in_arr)

out_arr = geek.argpartition(in_arr, 1, axis = 1)
print ("Output partitioned array indices :\n ", out_arr)
