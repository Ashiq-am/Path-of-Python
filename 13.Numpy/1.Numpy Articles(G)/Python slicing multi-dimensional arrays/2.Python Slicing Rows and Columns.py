import numpy as np

matrix = np.array([[1, 2, 3, 4],
				[5, 6, 7, 8],
				[9, 10, 11, 12]])

# Slicing with step
# Skip every other row and column
sliced_matrix = matrix[::2, ::2]
print(sliced_matrix)
