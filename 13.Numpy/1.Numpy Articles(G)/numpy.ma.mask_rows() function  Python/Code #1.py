# Python program explaining
# numpy.ma.mask_rowcols() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.zeros((4, 4), dtype = int)
arr[2, 2] = 1

arr = ma.masked_equal(arr, 1)

gfg = ma.mask_rows(arr)

print (gfg)
