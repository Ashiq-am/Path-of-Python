# Python program explaining
# numpy.ma.is_mask() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

m = ma.masked_equal([0, 1, 2, 0, 3], 0)

gfg = ma.is_mask(m)


print (gfg)
