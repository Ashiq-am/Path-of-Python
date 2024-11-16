# Python program explaining
# numpy.ma.masked_all_like() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.zeros((4, 3), dtype = geek.float32)

gfg = ma.masked_all_like(arr)

print (gfg)
