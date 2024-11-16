# Python program explaining
# numpy.atleast_3d() function
# when inputs are in high dimension

import numpy as geek

in_arr = geek.arange(16).reshape(1, 4, 4)
print ("Input array :\n ", in_arr)

out_arr = geek.atleast_3d(in_arr)
print ("output array :\n ", out_arr)
print(in_arr is out_arr)
