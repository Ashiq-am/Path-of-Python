# Program to concatenate two 2D arrays row-wise
import numpy as np


arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(10, 19).reshape(3, 3)

# Concatenating operation
# axis = 1 implies that it is being
# done row-wise
np.stack((arr1, arr2), axis=1)
