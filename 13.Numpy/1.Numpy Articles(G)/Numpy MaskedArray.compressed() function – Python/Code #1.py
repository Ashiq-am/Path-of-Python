# Python program explaining
# numpy.MaskedArray.compressed() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.ma.array(geek.arange(10), mask =[0]*6 + [1]*4)
gfg = arr.compressed()

print(gfg)
