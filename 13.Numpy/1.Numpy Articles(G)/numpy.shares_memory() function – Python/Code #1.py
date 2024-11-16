# Python program explaining
# numpy.shares_memory() function

# importing numpy as geek
import numpy as geek

arr1 = geek.array([1, 2, 3, 4])
arr2 = geek.array([5, 6, 7])

gfg = geek.shares_memory(arr1, arr2)

print(gfg)
