# Python program explaining
# numpy.ascontiguousarray() function

import numpy as geek

my_tuple = ([2, 6, 10], [8, 12, 16])

print("Input touple : ", my_tuple)

out_arr = geek.ascontiguousarray(my_tuple, dtype=geek.int32)
print("output array from input touple : ", out_arr)
