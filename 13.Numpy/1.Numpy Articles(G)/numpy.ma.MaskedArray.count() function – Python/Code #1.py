# Python program explaining
# numpy.ma.MaskedArray.count() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = ma.arange(6).reshape((2, 3))
arr[1, :] = ma.masked

gfg = arr.count(axis=0)

print(gfg)
