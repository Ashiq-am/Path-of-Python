# Python program explaining
# numpy.ma.ediff1d() function

# importing numpy as geek
import numpy as geek

arr = geek.array([3, 5, 8, 4, 12])

gfg = geek.ma.ediff1d(arr, to_begin=geek.array([-23, 0]), to_end=25)

print(gfg)
