# Python program explaining
# argwhere() function

import numpy as geek

# input array
in_arr = [[ 2, 0, 7], [ 0, 5, 9]]
print ("Input array : ", in_arr)

out_arr = geek.argwhere(in_arr)
print ("Output indices of non zero array element: \n", out_arr)
