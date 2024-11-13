# Input set of tuples
tuple_set = {(1, 2), (3, 4), (5, 6)}

# Convert set of tuples to list of lists using nested loops
list_of_lists = []
for t in tuple_set:
	list_of_lists.append(list(t))

# Output
print(list_of_lists)
