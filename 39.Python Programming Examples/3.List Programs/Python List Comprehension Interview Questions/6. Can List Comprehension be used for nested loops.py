a = [[1, 2], [3, 4], [5, 6]]

# Use list comprehension to flatten the 2D list into a 1D list
flattened = [item for sublist in a for item in sublist]
print(flattened)