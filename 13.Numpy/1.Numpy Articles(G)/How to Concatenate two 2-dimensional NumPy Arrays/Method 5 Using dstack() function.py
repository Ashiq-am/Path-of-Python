# Program to concatenate two 2D arrays
# along the height
import numpy as np

arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(10, 19).reshape(3, 3)

# Concatenating operation
arr = np.dstack((arr1, arr2))
