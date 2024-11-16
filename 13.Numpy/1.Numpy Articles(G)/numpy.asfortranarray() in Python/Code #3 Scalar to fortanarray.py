# Python program explaining
# numpy.asfortranarray() function

import numpy as geek

my_scalar = 15

print("Input scalar : ", my_scalar)

out_arr = geek.asfortranarray(my_scalar, dtype='float')
print("output fortan array from input scalar : ", out_arr)
