# Python program explaining
# numpy.ma.MaskedArray.toflex() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.ma.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]],
										mask =[0] + [1, 1]*4)

gfg = arr.toflex()

print (gfg)
