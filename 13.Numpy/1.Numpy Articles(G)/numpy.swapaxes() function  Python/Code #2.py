# Python program explaining
# numpy.swapaxes() function

# importing numpy as geek
import numpy as geek

arr = geek.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])

gfg = geek.swapaxes(arr, 0, 2)

print (gfg)
