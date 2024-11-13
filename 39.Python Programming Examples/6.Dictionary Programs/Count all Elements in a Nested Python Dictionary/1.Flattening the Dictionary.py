def flatten_dict(nested_dict):
	flat_dict = {}
	for key, value in nested_dict.items():
		if isinstance(value, dict):
			flat_dict.update(flatten_dict(value))
		else:
			flat_dict[key] = value
	return flat_dict

# Example
nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}
flat_dict = flatten_dict(nested_dict)
total_elements = len(flat_dict)
print(f"Total elements in the nested dictionary: {total_elements}")
