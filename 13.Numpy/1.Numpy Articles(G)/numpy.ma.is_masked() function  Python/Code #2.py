# Python program explaining
# numpy.ma.is_masked() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = [True, False, True]

# always returns False unless
# the input is a MaskedArray
gfg = ma.is_masked(arr)

print (gfg)
