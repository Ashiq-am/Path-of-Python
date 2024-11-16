# Program to concatenate two 2D arrays column-wise
# import numpy
import numpy as np

# Creating two 2D arrays
arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(10,19).reshape(3,3)
arr1
arr2

# Concatenating operation
# axis = 1 implies that it is being done column-wise
np.concatenate((arr1,arr2),axis=1)
