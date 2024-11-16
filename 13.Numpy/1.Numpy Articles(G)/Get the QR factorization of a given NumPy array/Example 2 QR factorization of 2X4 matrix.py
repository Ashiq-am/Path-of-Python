# Import numpy package
import numpy as np

# Create a numpy array
arr = np.array([[0, 1], [1, 0], [1, 1], [2, 2]])

# Find the QR factor of array
q, r = np.linalg.qr(arr)

# Print the result
print("Decomposition of matrix:")
print( "q=\n", q, "\nr=\n", r)
