list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for sublist in list_of_lists:
	for item in sublist:
		print(item, end=' ')
	print()
