# Python Program illustrating
# numpy.append()

import numpy as geek

#Working on 1D
arr1 = geek.arange(8).reshape(2, 4)
print("2D arr1 : \n", arr1)
print("Shape : ", arr1.shape)


arr2 = geek.arange(8, 16).reshape(2, 4)
print("\n2D arr2 : \n", arr2)
print("Shape : ", arr2.shape)


# appending the arrays
arr3 = geek.append(arr1, arr2)
print("\nAppended arr3 by flattened : ", arr3)

# appending the arrays with axis = 0
arr3 = geek.append(arr1, arr2, axis = 0)
print("\nAppended arr3 with axis 0 : \n", arr3)

# appending the arrays with axis = 1
arr3 = geek.append(arr1, arr2, axis = 1)
print("\nAppended arr3 with axis 1 : \n", arr3)
