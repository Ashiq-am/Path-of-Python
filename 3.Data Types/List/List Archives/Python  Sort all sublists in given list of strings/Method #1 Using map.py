# Python code to sort all sublists
# in given list of strings

# List initialization
Input = [['Machine', 'London', 'Canada', 'France', 'Lanka'],
		['Spain', 'Munich'],
		['Australia', 'Mandi']]

# Using map for sorting
Output = list(map(sorted, Input))

# Printing output
print(Output)
