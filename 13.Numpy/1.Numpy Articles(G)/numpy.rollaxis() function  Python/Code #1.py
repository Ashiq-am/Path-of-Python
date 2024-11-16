# Python program explaining
# numpy.rollaxis() function

# importing numpy as geek
import numpy as geek

arr = geek.ones((1, 2, 3, 4))

gfg = geek.rollaxis(arr, 3, 1).shape

print (gfg)
