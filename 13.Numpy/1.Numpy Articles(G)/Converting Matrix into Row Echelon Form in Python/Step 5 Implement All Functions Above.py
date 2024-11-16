def row_echelon_form(matrix):
	nrows = matrix.shape[0]
	ncols = matrix.shape[1]
	pivot_row = 0
# this will run for number of column times. If matrix has 3 columns this loop will run for 3 times
	for col in range(ncols):
		nonzero_row = find_nonzero_row(matrix, pivot_row, col)
		if nonzero_row is not None:
			swap_rows(matrix, pivot_row, nonzero_row)
			make_pivot_one(matrix, pivot_row, col)
			eliminate_below(matrix, pivot_row, col)
			pivot_row += 1
	return matrix
