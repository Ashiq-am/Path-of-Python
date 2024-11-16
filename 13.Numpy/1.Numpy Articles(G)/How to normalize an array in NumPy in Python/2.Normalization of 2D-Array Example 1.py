# import module
import numpy as np

# explicit function to normalize array
def normalize_2d(matrix):
	norm = np.linalg.norm(matrix)
	matrix = matrix/norm # normalized matrix
	return matrix

# gives and array staring from -2
# and ending at 13
array = np.arange(16) - 2

# coverts 1d array to a matrix
matrix = array.reshape(4, 4)
print("Simple Matrix \n", matrix)
normalized_matrix = normalize_2d(matrix)
print("\nSimple Matrix \n", normalized_matrix)
