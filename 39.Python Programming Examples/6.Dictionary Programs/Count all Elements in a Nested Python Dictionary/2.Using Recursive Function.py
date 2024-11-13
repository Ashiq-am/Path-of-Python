def count_elements_nested_dict(nested_dict):
	count = 0
	for value in nested_dict.values():
		if isinstance(value, dict):
			count += count_elements_nested_dict(value)
		else:
			count += 1
	return count

# Example
nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}
total_elements = count_elements_nested_dict(nested_dict)
print(f"Total elements in the nested dictionary: {total_elements}")
