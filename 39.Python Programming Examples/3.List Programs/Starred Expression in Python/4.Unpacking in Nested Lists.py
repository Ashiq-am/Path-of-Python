# Example list with nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Unpack the nested lists using starred expressions
*row1, = matrix[0]
*row2, = matrix[1]
*row3, = matrix[2]

# Print the results
print("Row 1:", row1)
print("Row 2:", row2)
print("Row 3:", row3)
