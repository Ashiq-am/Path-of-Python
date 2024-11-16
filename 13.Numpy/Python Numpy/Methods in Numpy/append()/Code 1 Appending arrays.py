# Python Program illustrating
# numpy.append()

import numpy as geek

#Working on 1D
arr1 = geek.arange(5)
print("1D arr1 : ", arr1)
print("Shape : ", arr1.shape)


arr2 = geek.arange(8, 12)
print("\n1D arr2 : ", arr2)
print("Shape : ", arr2.shape)


# appending the arrays
arr3 = geek.append(arr1, arr2)
print("\nAppended arr3 : ", arr3)
