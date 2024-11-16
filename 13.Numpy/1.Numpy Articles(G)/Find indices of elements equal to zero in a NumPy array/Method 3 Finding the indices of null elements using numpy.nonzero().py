# importing Numpy package
import numpy as np

# creating a 1-D Numpy array
n_array = np.array([1, 10, 2, 0, 3, 9, 0,
					5, 0, 7, 5, 0, 0])

print("Original array:")
print(n_array)

# finding indices of null elements using
# np.nonzero()
print("\nIndices of null elements:")

res = np.nonzero(n_array == 0)
print(res)
