# Python program explaining
# numpy.ma.notmasked_contiguous() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.arange(12).reshape((3, 4))
mask = geek.zeros_like(arr)
mask[1:, :-1] = 1; mask[0, 1] = 1; mask[-1, 0] = 0
ma = geek.ma.array(arr, mask = mask)

gfg = geek.ma.notmasked_contiguous(ma, axis = 1)

print (gfg)
