import numpy as np

# NumPy array with elements from 1 to 9
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Index values can be negative.
arr = x[np.array([1, 3, -3])]
print("\n Elements are : \n",arr)
