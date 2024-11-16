# Python Program illustrating
# numpy.delete()

import numpy as geek

#Working on 1D
arr = geek.arange(5)
print("arr : \n", arr)
print("Shape : ", arr.shape)

# deletion from 1D array

object = 2
a = geek.delete(arr, object)
print("\ndeleteing arr 2 times : \n", a)
print("Shape : ", a.shape)

object = [1, 2]
b = geek.delete(arr, object)
print("\ndeleteing arr 3 times : \n", b)
print("Shape : ", a.shape)
