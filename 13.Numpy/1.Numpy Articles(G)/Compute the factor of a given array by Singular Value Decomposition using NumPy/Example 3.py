# Import numpy library
import numpy as np

# Create a numpy array
arr = np.array([[8, 1], [0, 5]], dtype=np.float32)
print("Original array:")
print(arr)

# Compute the factor
U, s, V = np.linalg.svd(arr, full_matrices=False)

# Print the result
print("\nFactor of the given array by Singular Value Decomposition:")
print("\nU=", U, "\n\ns=", s, "\n\nV=", V)
