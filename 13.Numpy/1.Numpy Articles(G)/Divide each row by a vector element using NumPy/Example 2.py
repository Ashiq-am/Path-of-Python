# Importing Numpy module
import numpy as np

# Creating 2-D Numpy array
n_arr = np.array([[20, 35, 40],
				[10, 51, 25]])

print("Given 2-D Array:")
print(n_arr)

# Vector element
vec = np.array([2.5])
print("\nVector element:")
print(vec)

# Dividing rows of 2-D array with vector element
print("\nResultant Array")
print(n_arr / vec[:,None])
