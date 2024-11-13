# Python code to find whether a sublist
# satisfies the triangle inequality.

# List initialization
Input = [[1, 3, 1], [4, 5, 6]]

# Sorting sublist
for elem in Input:
	elem.sort()

# Using list comprehension
Output = [(p, q, r) for p, q, r in Input if (p + q)>= r]

# Printing output
print(Output)
