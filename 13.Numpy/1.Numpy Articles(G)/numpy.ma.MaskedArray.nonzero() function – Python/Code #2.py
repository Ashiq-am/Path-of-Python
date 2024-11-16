# Python program explaining
# numpy.ma.MaskedArray.nonzero() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = ma.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

gfg = ma.nonzero(arr > 3)

print(gfg)
