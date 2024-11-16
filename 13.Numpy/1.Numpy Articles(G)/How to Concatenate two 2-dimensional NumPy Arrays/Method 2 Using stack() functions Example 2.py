# Program to concatenate two 2D arrays along
# the height
import numpy as np

arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(10, 19).reshape(3, 3)

# Concatenating operation
# axis = 2 implies that it is being done
# along the height
np.stack((arr1, arr2), axis=2)
