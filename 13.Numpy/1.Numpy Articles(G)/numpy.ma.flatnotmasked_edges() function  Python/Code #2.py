# Python program explaining
# numpy.ma.flatnotmasked_edges() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.ma.arange(12)
arr[:] = geek.ma.masked

gfg = geek.ma.flatnotmasked_edges(arr)

print (gfg)
