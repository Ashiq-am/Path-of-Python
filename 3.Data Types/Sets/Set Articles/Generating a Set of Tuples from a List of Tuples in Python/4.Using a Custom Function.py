# Sample list of tuples
list_of_tuples = [(1, 2), (3, 4), (1, 2), (5, 6)]

# Custom function to create a set of tuples
def unique_tuples(input_list):
	seen = set()
	result = set()
	for item in input_list:
		if item not in seen:
			seen.add(item)
			result.add(item)
	return result

# Generate a set of tuples using the custom function
set_of_tuples = unique_tuples(list_of_tuples)

# Display the result
print(set_of_tuples)
