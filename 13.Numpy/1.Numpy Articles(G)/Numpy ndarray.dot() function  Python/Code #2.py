# Python program explaining
# numpy.ndarray.dot() function

# importing numpy as geek
import numpy as geek

arr1 = geek.eye(3)
arr = geek.ones((3, 3)) * 3

gfg = arr1.dot(arr).dot(arr)

print( gfg)
