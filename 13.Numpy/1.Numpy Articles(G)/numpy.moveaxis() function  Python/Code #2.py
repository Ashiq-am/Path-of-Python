# Python program explaining
# numpy.moveaxis() function

# importing numpy as geek
import numpy as geek

arr = geek.zeros((1, 2, 3, 4))

gfg = geek.moveaxis(arr, -1, 0).shape

print (gfg)
