n = int(input("Enter the number of rows: "))
jagged_arr = []

for i in range(n):
	k = int(input(f"Enter the number of columns in row {i + 1}: "))
	row = []
	for j in range(k):
		x = int(input(f"Enter the value for row {i + 1}, column {j + 1}: "))
		row.append(x)
	jagged_arr.append(row)
