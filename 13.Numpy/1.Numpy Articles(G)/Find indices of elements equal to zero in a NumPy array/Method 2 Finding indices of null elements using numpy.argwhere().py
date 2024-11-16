# importing Numpy package
import numpy as np

# creating a 3-D Numpy array
n_array = np.array([[0, 2, 3],
					[4, 1, 0],
					[0, 0, 2]])

print("Original array:")
print(n_array)

# finding indices of null elements
# using np.argwhere()
print("\nIndices of null elements:")
res = np.argwhere(n_array == 0)

print(res)
