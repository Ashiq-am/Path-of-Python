# Replication with *
rows, cols = 3, 4
row_template = [0] * cols
matrix = [row_template[:] for _ in range(rows)]

# Print the initialized list of lists
print(matrix)
