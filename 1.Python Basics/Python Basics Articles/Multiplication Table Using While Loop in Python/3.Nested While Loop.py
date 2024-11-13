# Nested While Loop (Left-to-Right Format)
row = 1

while row <= 10:
	col = 1
	while col <= 10:
		result = row * col
		print(f"{row} x {col} = {result}", end="\t")
		col += 1
	print() # Move to the next line for the next row
	row += 1
