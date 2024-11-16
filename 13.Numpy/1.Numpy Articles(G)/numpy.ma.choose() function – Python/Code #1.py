# Python program explaining
# numpy.ma.choose() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

choice = geek.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
arr = geek.array([2, 1, 0])

gfg = geek.ma.choose(arr, choice)

print(gfg)
