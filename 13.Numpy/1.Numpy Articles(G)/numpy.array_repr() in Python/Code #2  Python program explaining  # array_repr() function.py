# Python program explaining
# array_repr() function

import numpy as geek

in_arr = geek.array([5e-8, 4e-7, 8, -4])

print("Input array : ", in_arr)
print(type(in_arr))

out_arr = geek.array_repr(in_arr, precision=6, suppress_small=True)
print("The string representation of input array : ", out_arr)
print(type(out_arr))
