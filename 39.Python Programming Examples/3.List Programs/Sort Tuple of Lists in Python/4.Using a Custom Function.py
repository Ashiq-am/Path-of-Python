# Define a tuple of lists
tuple_of_lists = ([2, 1, 5], [1, 5, 7], [5, 6, 5])

# Define a custom function to sort each inner list
def sort_inner_list(inner_list):
	return sorted(inner_list)

# Sort each inner list using the custom function and create a new tuple
sorted_tuple = tuple(map(sort_inner_list, tuple_of_lists))

print(sorted_tuple)
