# Python program explaining
# numpy.MaskedArray.compressed() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.ma.array(geek.arange(7), mask =[0]*4 + [1]*3)
gfg = arr.compressed()

print(gfg)
