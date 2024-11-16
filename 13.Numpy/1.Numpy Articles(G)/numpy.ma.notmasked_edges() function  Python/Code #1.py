# Python program explaining
# numpy.ma.notmasked_edges() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.arange(12).reshape((3, 4))

gfg = geek.ma.notmasked_edges(arr)

print (gfg)
