# Program to concatenate two 2D arrays row-wise
import numpy as np

# Creating two 2D arrays
arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(10, 19).reshape(3, 3)

# Concatenating operation
# axis = 0 implies that it is being done row-wise
np.concatenate((arr1, arr2), axis=0)
