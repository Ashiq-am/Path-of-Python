# Python program explaining
# numpy.ma.masked_values() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.array([1, 2, 3, 4, 5, 6])

gfg = ma.masked_values(arr, 4)

print (gfg)
