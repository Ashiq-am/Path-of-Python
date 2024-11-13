import itertools

# Flattening a list of lists using a loop
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []
for sublist in lists:
	for item in sublist:
		flattened.append(item)
print(flattened)

# Flattening a list of lists using itertools
flattened = list(itertools.chain(*lists))
print(flattened)
