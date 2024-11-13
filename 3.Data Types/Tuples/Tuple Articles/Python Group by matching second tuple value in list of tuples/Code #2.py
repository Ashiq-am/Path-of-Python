# Python program to group tuples by matching
# second tuple value in list of tuples

# Initialisation
Input = [(20, 'Geek'), (31, 'Geek'), (88, 'NotGeek'), (27, 'NotGeek')]

Output = {}
for x, y in Input:
	if y in Output:
		Output[y].append((x, y))
	else:
		Output[y] = [(x, y)]

# Printing Output
print(Output)
