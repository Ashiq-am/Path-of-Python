def find_nonzero_row(matrix, pivot_row, col):
	nrows = matrix.shape[0]
	for row in range(pivot_row, nrows):
		if matrix[row, col] != 0:
			return row
	return None
