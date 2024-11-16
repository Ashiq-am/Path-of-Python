# Python program explaining
# partition() function

import numpy as geek

# input array
in_arr = geek.array([ 2, 0, 1, 5, 4, 9, 3])
print ("Input array : ", in_arr)

out_arr = geek.partition(in_arr, (0, 3))
print ("Output partitioned array : ", out_arr)
