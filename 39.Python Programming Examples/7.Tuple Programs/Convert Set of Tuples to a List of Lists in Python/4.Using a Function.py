# Function to convert a set of tuples to a list of lists
def convert_to_list_of_lists(tuple_set):
	return [list(t) for t in tuple_set]

# Input set of tuples
tuple_set = {(1, 2), (3, 4), (5, 6)}

# Convert set of tuples to list of lists using a function
list_of_lists = convert_to_list_of_lists(tuple_set)

# Output
print(list_of_lists)
