list_of_sets = [{1, 2, 3}, {2, 3, 4}, {1, 2, 3}]

# Using a set and list comprehension to remove duplicates
unique_list = []

for s in {frozenset(s) for s in list_of_sets}:
	unique_list.append(set(s))
print(unique_list)
