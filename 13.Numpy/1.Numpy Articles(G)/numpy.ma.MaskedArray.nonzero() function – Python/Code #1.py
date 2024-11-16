# Python program explaining
# numpy.ma.MaskedArray.nonzero() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = ma.array(geek.eye(5))

gfg = arr.nonzero()

print(gfg)
