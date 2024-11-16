# import module
import numpy as np

def normalize_2d(matrix):
	# Only this is changed to use 2-norm put 2 instead of 1
	norm = np.linalg.norm(matrix, 1)
	# normalized matrix
	matrix = matrix/norm
	return matrix

# gives and array staring from -2 and ending at 13
array = np.arange(16) - 2
# coverts 1d array to a matrix
matrix = array.reshape(4, 4)
print("Simple Matrix \n", matrix)
normalized_matrix = normalize_2d(matrix)
print("\nSimple Matrix \n", normalized_matrix)
