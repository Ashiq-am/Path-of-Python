list_of_sets = [{1, 2, 3}, {2, 3, 4}, {2, 1, 3}]

# Using a loop and not in to remove duplicates
unique_list = []

# iterating list
for s in list_of_sets:
	if s not in unique_list:
		unique_list.append(s)

print(unique_list)
