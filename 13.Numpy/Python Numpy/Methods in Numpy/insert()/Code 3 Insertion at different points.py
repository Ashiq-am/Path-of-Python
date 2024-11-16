# Python Program illustrating
# numpy.insert()

import numpy as geek

#Working on 1D
arr = geek.arange(6).reshape(2, 3)
print("1D arr : \n", arr)
print("Shape : ", arr.shape)

# value = 9
# index = 1
# Insertion before first index
a = geek.insert(arr, (2, 4), 9)
print("\nInsertion at two points : ", a)
print("Shape : ", a.shape)


# Working on 2D array
arr = geek.arange(12).reshape(3, 4)
print("\n\n2D arr : \n", arr)
print("Shape : ", arr.shape)
a = geek.insert(arr, (0, 3), 66, axis = 1)
print("\nInsertion at two points : \n", a)
print("Shape : ", a.shape)
