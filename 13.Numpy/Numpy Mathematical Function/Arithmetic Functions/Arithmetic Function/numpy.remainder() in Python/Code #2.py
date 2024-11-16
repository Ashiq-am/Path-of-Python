# Python program explaining
# numpy.remainder() function

import numpy as geek

in_arr1 = geek.array([5, -4, 8])
in_arr2 = geek.array([2, 3, 4])

print("Dividend array : ", in_arr1)
print("Divisor array : ", in_arr2)

out_arr = geek.remainder(in_arr1, in_arr2)
print("Output remainder array: ", out_arr)
