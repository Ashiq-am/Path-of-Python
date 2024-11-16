# Python program explaining
# numpy.ma.masked_values() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.array([1, 1.5, 2, 1.5, 3])

gfg = ma.masked_values(arr, 1.5)

print (gfg)
