# Python program explaining
# numpy.ma.clump_unmasked() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.ma.masked_array(geek.arange(8))
arr[[0, 1, 2, 6]] = geek.ma.masked

gfg = geek.ma.clump_unmasked(arr)

print (gfg)
