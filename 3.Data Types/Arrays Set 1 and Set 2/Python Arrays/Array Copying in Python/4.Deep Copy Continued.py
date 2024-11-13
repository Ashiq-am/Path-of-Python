import copy


def rotate_matrix(image):
	# Copy method one
	copy_image_one = copy.deepcopy(image)
	print("Original", matrix)
	print("Copy of original", copy_image_one)
	N = len(matrix)

	# Part 1, reverse order within each row
	for row in range(N):
		for column in range(N):
			copy_image_one[row][column] = image[row][N-column-1]

	print("After modification")
	print("Original", matrix)
	print("Copy", copy_image_one)

	# Copy method two
	copy_image_two = [list(row) for row in copy_image_one]
	# Test on what happens when you remove list from the above code.

	# Part 2, transpose
	for row in range(N):
		for column in range(N):
			copy_image_two[column][row] = copy_image_one[row][column]

	return copy_image_two


if __name__ == "__main__":
	matrix = [[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]]
	print("Rotated image", rotate_matrix(matrix))
