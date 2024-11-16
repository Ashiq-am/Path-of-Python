# Python program explaining
# numpy.ma.clump_masked() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.ma.masked_array(geek.arange(10))
arr[[0, 1, 2, 6, 8, 9]] = geek.ma.masked

gfg = geek.ma.clump_masked(arr)

print (gfg)
