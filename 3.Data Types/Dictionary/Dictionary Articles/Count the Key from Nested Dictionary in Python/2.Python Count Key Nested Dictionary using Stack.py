# Function to count keys in a nested dictionary using a stack and iteration
def count_keys_iterative(dictionary):
	stack = [dictionary]
	count = 0
	while stack:
		current_dict = stack.pop()
		count += len(current_dict)
		stack.extend(value for value in current_dict.values()
					if isinstance(value, dict))
	return count

# Example Usage:
nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}
result = count_keys_iterative(nested_dict)
print("Total number of keys in the nested dictionary:", result)
