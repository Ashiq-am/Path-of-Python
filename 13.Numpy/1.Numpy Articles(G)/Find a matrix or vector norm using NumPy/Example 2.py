# import library
import numpy as np

# initialize matrix
mat = np.array([[ 1, 2, 3],
			[4, 5, 6]])

# compute norm of matrix
mat_norm = np.linalg.norm(mat)

print("Matrix norm:")
print(mat_norm)
