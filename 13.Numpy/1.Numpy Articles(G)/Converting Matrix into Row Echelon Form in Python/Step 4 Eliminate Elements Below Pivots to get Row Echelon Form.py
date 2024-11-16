def eliminate_below(matrix, pivot_row, col):
	nrows = matrix.shape[0]
	pivot_element = matrix[pivot_row, col]
	for row in range(pivot_row + 1, nrows):
		factor = matrix[row, col]
		matrix[row] -= factor * matrix[pivot_row]
