# Python program explaining
# numpy.asarray_chkfinite() function
# when value error occurs

import numpy as geek

my_list = [1, 3, 5, 7, geek.inf, geek.nan]

print("Input scalar : ", my_scalar)

out_arr = geek.asarray_chkfinite(my_list)
print("output fortan array from input scalar : ", out_arr)
