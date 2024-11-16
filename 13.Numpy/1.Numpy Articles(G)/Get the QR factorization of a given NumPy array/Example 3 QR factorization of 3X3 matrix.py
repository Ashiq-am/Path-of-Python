# Import numpy package
import numpy as np

# Create a numpy array
arr = np.array([[5, 11, -15], [12, 34, -51],
				[-24, -43, 92]], dtype=np.int32)

# Find the QR factor of array
q, r = np.linalg.qr(arr)

# Print the result
print("Decomposition of matrix:")
print( "q=\n", q, "\nr=\n", r)
