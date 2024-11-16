import numpy as np

matrix = np.array([[1, 2, 3],
				[4, 5, 6],
				[7, 8, 9]])

# Slicing a subarray
# Get a 2x2 subarray
sub_matrix = matrix[0:2, 1:3]
print(sub_matrix)
