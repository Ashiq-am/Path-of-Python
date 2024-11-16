# Python program explaining
# argpartition() function

import numpy as geek

# input array
in_arr = geek.array([ 2, 0, 1, 5, 4, 3])
print ("Input array : ", in_arr)

out_arr = geek.argpartition(in_arr, (0, 2))
print ("Output partitioned array indices: ", out_arr)
