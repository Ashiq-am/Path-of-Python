# Python program explaining
# numpy.concatenate() function

# importing numpy as geek
import numpy as geek

arr1 = geek.array([[2, 4], [6, 8]])
arr2 = geek.array([[3, 5], [7, 9]])

gfg = geek.concatenate((arr1, arr2), axis = 0)

print (gfg)
