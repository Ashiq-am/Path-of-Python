import numpy as np

# Creating a 1D array and a 2D array
array1 = np.array([1, 2, 3])
array2 = np.array([[10], [20], [30]])

# Broadcasting operation
result = array1 + array2
print("Broadcasting Result:\n", result)