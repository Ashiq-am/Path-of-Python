# Python code to count unique sublist within list

# Input list initialization
Input = [['Geek', 'for', 'geeks'], ['geeks', 'for'],
		['for', 'Geeks', 'geek'], ['Geek', 'for', 'geeks']]

# Output list initialization
Output = {}

# Using Iteration
for lis in Input:
	Output.setdefault(tuple(lis), list()).append(1)
for a, b in Output.items():
	Output[a] = sum(b)

# Printing output
print(Output)
