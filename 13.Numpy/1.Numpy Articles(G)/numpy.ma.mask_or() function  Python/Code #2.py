# Python program explaining
# numpy.ma.mask_or() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

m1 = geek.ma.make_mask([1, 0, 0, 0])
m2 = geek.ma.make_mask([1, 1, 0, 1])

gfg = geek.ma.mask_or(m1, m2)

print (gfg)
