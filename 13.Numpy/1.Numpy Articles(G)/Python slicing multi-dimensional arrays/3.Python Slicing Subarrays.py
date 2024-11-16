# Create a sample 2-D array (a list of lists)
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

# Slicing using negative indexing to get the last row
last_row = matrix[-1]
print("Last Row:", last_row)

# Slicing using negative indexing to get the last element of the first row
last_element_first_row = matrix[0][-1]
print("Last Element of First Row:", last_element_first_row)

# Slicing using negative indexing to get the last two elements of the second row
last_two_elements_second_row = matrix[1][-2:]
print("Last Two Elements of Second Row:", last_two_elements_second_row)
