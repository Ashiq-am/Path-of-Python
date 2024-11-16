# Python program explaining
# numpy.ascontiguousarray() function

import numpy as geek

my_scalar = 100

print("Input scalar : ", my_scalar)

out_arr = geek.ascontiguousarray(my_scalar, dtype=geek.float32)
print("output array from input scalar : ", out_arr)
print(type(out_arr))
