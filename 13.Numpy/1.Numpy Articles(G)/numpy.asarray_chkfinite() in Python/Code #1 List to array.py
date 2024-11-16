# Python program explaining
# numpy.asarray_chkfinite() function

import numpy as geek

my_list = [1, 3, 5, 7, 9]

print("Input list : ", my_list)

out_arr = geek.asarray_chkfinite(my_list, dtype='float')
print("output array from input list : ", out_arr)
