# python Program to read a square matrix
# and print the elements below main diagonal


if __name__ == "__main__":

	matrix = [[0 for x in range(5)]for y in range(5)]
	x = 0
	size = 5

	# Get the square matrix
	for row_index in range(0, size):
		for column_index in range(0, size):
			x += 1
			matrix[row_index][column_index] = x

	# Display the matrix
	print("The matrix is")
	for row_index in range(0, size):
		for column_index in range(0, size):

			print(matrix[row_index][column_index], end=" ")

		print()
	# Print the elements below main diagonal
	print()
	print("Elements below Main diagonal elements are:")

	for row_index in range(0, size):
		for column_index in range(0, size):

			# check for elements below main diagonal
			if (row_index > column_index):
				print(matrix[row_index][column_index], end=", ")
