# Python code to find the index at which the
# element of two list doesn't match.

# List initialisation
Input1 = [1, 2, 3, 4]
Input2 = [1, 5, 3, 6]

# Using list comprehension and zip
Output = [Input2.index(y) for x, y in
	zip(Input1, Input2) if y != x]

# Printing output
print(Output)
