# importing libraries
import numpy as np

# row_stacking array
a = np.array([1, 2, 3])
arr = np.ma.row_stack (a)

print ("arr : \n", arr)

# row_stacking array
b = np.array([[1], [2], [3]])
arr1 = np.ma.row_stack (b)

print ("\narr1 : \n", arr1)
