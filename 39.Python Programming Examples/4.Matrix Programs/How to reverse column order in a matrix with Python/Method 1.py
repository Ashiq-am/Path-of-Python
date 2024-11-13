# creating a 3X4 matrix using nested lists
matrix_1 = [['c1', 'c2', 'c3'],
			[10, 20, 30],
			[40, 50, 60],
			[70, 80, 90]]

# creating an empty array to store the reversed coulumn matrix
matrix_2 = []

# looping through matrix_1 and appending matrix_2
for i in range(len(matrix_1)):
	matrix_2.append(matrix_1[i][::-1])

print('Matrix before changing column order:\n')
for rows in matrix_1:
	print(rows)
print('\nMatrix after changing column order:\n')
for rows in matrix_2:
	print(rows)
