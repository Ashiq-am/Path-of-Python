# Python code to find the tuples containing
# the given element from a list of tuples

# List of tuples
Input = [(11, 22), (33, 55), (55, 77),
		(11, 44), (33, 22, 100, 11), (99, 11)]

# Using filter
Output = list(filter(lambda x:11 in x, Input))

# Prinitng output
print(Output)
