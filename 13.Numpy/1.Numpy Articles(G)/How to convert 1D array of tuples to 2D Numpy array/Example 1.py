# importing Numpy
import numpy as np

# 1d Array of Tuple
arr = [(1, 2, 3), ('Hi', 'Hello', 'Hey')]
x = map(np.array, arr)

# Changing map object to a list, then
# to an NDarray
x = np.array(list(x))
print(x)

# Checking the Dimension of the Resulting
# NDArray
print(x.ndim)
