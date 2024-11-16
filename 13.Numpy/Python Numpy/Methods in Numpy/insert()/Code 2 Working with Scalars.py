# Python Program illustrating
# numpy.insert()

import numpy as geek

# Working on 2D array
arr = geek.arange(12).reshape(3, 4)
print("2D arr : \n", arr)
print("Shape : ", arr.shape)

# Working with Scalars
a = geek.insert(arr, [1], [[6],[9],], axis = 0)
print("\nArray after insertion : \n", a)
print("Shape : ", a.shape)

# Working with Scalars
a = geek.insert(arr, [1], [[8],[7],[9]], axis = 1)
print("\nArray after insertion : \n", a)
print("Shape : ", a.shape)
