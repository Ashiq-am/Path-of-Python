# Initializing a list of lists
list_of_lists = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

# Traversing the list of lists using nested loops
for row in list_of_lists:
	for element in row:
		print(element, end=' ')
	print()
