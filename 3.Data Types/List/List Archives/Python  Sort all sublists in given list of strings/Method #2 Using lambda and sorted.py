# Python code to sort all sublists
# in given list of strings

# List initialization
Input = [['Machine', 'London', 'Canada', 'France', 'Lanka'],
		['Spain', 'Munich'],
		['Australia', 'Mandi']]

# using lambda and sorted
Output = [sorted(x, key = lambda x:x[0]) for x in Input]

# Printing output
print(Output)
