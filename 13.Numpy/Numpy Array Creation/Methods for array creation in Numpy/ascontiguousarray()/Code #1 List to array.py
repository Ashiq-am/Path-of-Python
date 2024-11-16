# Python program explaining
# numpy.ascontiguousarray() function

import numpy as geek

my_list = [100, 200, 300, 400, 500]

print("Input list : ", my_list)

out_arr = geek.ascontiguousarray(my_list, dtype=geek.float32)
print("output array from input list : ", out_arr)
