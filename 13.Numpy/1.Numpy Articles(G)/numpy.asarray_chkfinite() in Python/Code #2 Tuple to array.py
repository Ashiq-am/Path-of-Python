# Python program explaining
# numpy.asarray_chkfinite() function

import numpy as geek

my_tuple = ([1, 3, 9], [8, 2, 6])

print("Input tuple : ", my_tuple)

out_arr = geek.asarray_chkfinite(my_tuple, dtype='int8')
print("output array from input tuple : ", out_arr)
