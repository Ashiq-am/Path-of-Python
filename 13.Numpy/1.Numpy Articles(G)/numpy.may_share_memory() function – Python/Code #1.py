# Python program explaining
# numpy.may_share_memory() function

# importing numpy as geek
import numpy as geek

arr1 = geek.array([1, 2, 3, 4])
arr2 = geek.array([5, 6, 7])

gfg = geek.may_share_memory(arr1, arr2)

print(gfg)
