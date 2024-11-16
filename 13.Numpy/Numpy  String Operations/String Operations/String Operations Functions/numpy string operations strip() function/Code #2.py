# Python program explaining
# numpy.char.strip() method

import numpy as geek

# input arrays
in_arr = geek.array(['Sun', ' Moon ', 'Star'])
print ("Input array : ", in_arr)

out_arr = geek.char.strip(in_arr, chars ='Sun')

# 'Sun' removed from arr[0] as we have set chars = Sun
print ("Output array: ", out_arr)
