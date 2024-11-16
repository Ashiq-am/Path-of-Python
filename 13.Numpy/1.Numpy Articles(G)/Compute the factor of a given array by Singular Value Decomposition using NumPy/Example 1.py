# Import numpy library
import numpy as np

# Create a numpy array
arr = np.array([[0, 0, 0, 0, 1], [2, 0, 0, 1, 3],
				[4, 0, 2, 0, 0], [3, 2, 0, 0, 1]],
			dtype=np.float32)

print("Original array:")
print(arr)

# Compute the factor by Singular Value
# Decomposition
U, s, V = np.linalg.svd(arr, full_matrices=False)

# Print the result
print("\nFactor of the given array by Singular Value Decomposition:")
print("\nU=", U, "\n\ns=", s, "\n\nV=", V)
