# Python program explaining
# numpy.ma.mask_cols() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.zeros((3, 3), dtype = int)
arr[1, 1] = 1

arr = ma.masked_equal(arr, 1)

gfg = ma.mask_cols(arr)

print (gfg)
