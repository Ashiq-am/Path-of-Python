# Python program explaining
# numpy.ma.append() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr1 = ma.masked_values([1, 2, 3, 4], 2)
arr2 = ma.masked_values([[5, 6, 7], [8, 9, 10]], 8)

gfg = ma.append(arr1, arr2)

print (gfg)
