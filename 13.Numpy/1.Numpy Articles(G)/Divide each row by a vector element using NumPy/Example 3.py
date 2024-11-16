# Importing Numpy module
import numpy as np

# Creating 3-D Numpy array
n_arr = np.array([[[10, 25], [30, 45]],
				[[50, 65], [70, 85]]])

print("Given 3-D Array:")
print(n_arr)

# Vector element
vec = np.array([3, 3])
print("\nVector element:")
print(vec)

# Dividing rows of 3-D array with vector element
print("\nResultant Array")
print(n_arr / vec[:,None])
