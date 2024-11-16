def make_pivot_one(matrix, pivot_row, col):
	pivot_element = matrix[pivot_row, col]
	matrix[pivot_row] //= pivot_element
