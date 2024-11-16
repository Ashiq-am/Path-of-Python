# code to find the cofactor of given matrix
import numpy as np

def matrix_cofactor(matrix):

	cofactor = None
	cofactor = np.linalg.inv(matrix).T * np.linalg.det(matrix)

	# return cofactor matrix of the given matrix
	return cofactor

print(matrix_cofactor([[1, 2], [3, 4]]))
