# Python program explaining
# numpy.atleast_2d() function
# when inputs are in high dimension

import numpy as geek

in_arr = geek.arange(9).reshape(3, 3)
print ("Input array :\n ", in_arr)

out_arr = geek.atleast_2d(in_arr)
print ("output array :\n ", out_arr)
print(in_arr is out_arr)
