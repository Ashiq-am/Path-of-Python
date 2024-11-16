# Python program explaining
# numpy.ma.MaskedArray.toflex() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.ma.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
								mask =[0] + [1, 0]*4)

gfg = arr.toflex()

print (gfg)
