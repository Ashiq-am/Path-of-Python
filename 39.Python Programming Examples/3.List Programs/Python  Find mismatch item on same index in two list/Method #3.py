# Python code to find the index at which the
# element of two list doesn't match.

# List initialisation
Input1 = [1, 2, 3, 4]
Input2 = [1, 5, 3, 6]

# Using list comprehension and enumerate
Output = [index for index, elem in enumerate(Input2)
						if elem != Input1[index]]

# Printing output
print(Output)
