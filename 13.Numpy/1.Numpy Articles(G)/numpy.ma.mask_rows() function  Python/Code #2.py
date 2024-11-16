# Python program explaining
# numpy.ma.mask_rows() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.zeros((5, 5), dtype = int)
arr[3, 3] = 1

arr = ma.masked_equal(arr, 1)

gfg = ma.mask_rows(arr)

print (gfg)
