# Python program explaining
# numpy.may_share_memory() function

# importing numpy as geek
import numpy as geek

arr1 = geek.zeros([3, 4])
arr2 = arr1[::1]

gfg = geek.may_share_memory(arr1, arr2)

print(gfg)
