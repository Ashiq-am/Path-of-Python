# Python program explaining
# numpy.MaskedArray.filled() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = geek.ma.array([2, 4, 6, 8, 10], mask =[0, 0, 1, 0, 1],
										fill_value = -999)
gfg = arr.filled()

print(gfg)
