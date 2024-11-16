# Python program explaining
# numpy.asfortranarray() function

import numpy as geek

in_arr = geek.arange(9).reshape(3, 3)

print ("Input array : ", in_arr)

# checking if it is fortanarray
print(in_arr.flags['F_CONTIGUOUS'])

out_arr = geek.asfortranarray(in_arr, dtype ='float')
print ("output array from input array : ", out_arr)

# checking if it has become fortanarray
print(out_arr.flags['F_CONTIGUOUS'])
