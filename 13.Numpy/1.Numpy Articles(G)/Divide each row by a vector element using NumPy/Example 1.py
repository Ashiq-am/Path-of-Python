# Importing Numpy module
import numpy as np

# Creating 1-D Numpy array
n_arr = np.array([20, 30, 40])
print("Given 1-D Array:")
print(n_arr)

# Vector element
vec = np.array([12])
print("\nVector element:")
print(vec)

# Dividing rows of 1-D array with vector element
print("\nResultant Array")
print(n_arr / vec[:,None])
