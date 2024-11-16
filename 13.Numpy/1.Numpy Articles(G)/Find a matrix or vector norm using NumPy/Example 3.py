# import library
import numpy as np


mat = np.array([[ 1, 2, 3],
			[4, 5, 6]])

# compute matrix num along axis
mat_norm = np.linalg.norm(mat, axis = 1)

print("Matrix norm along particular axis :")
print(mat_norm)
