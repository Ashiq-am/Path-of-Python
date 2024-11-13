# Python code to remove tuples having
# duplicate first value from given
# list of tuples

# Input list initialization
Input = [(12.121, 'Geeksforgeeks is best'),
		(19212.22, 'India is best'),
		(12.121, 'Cyware is best.'),
		(923232.2323, 'Jiit is best')]

# using set
visited = set()

# Output list initialization
Output = []

# Iteration
for a, b in Input:
	if not a in visited:
		visited.add(a)
		Output.append((a, b))

# Printing
print("Initial list of tuple is \n", Input)
print("List of tuple after removing duplicates:\n ", Output)
