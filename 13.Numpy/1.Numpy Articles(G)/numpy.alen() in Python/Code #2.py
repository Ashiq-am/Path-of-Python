# Python program explaining
# alen() function

import numpy as geek

# input array(1 * 3*3)
in_arr = geek.arange(9).reshape(1, 3, 3)
print ("Input array : \n", in_arr)

out_dim = geek.alen(in_arr)
print ("Length of the first dimension of arr: ", out_dim)
