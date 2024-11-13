def count_keys(d):
	keys = 0

	if isinstance(d, dict):
		for item in d.keys():
			keys += 1
			if isinstance(d[item], (list, tuple, dict)):
				keys += count_keys(d[item])

	elif isinstance(d, (list, tuple)):
		for item in d:
			if isinstance(item, (list, tuple, dict)):
				keys += count_keys(item)

	return keys

# Example usage
nested_dict = {'Dict1': {'name': 'Alice', 'age': '22', 'address': {'city': 'Wonderland'}},
			'Dict2': {'name': 'Bob', 'age': '28', 'contacts': {'email': 'bob@example.com'}}}

keys_count = count_keys(nested_dict)
print("Total number of keys in the nested dictionary:", keys_count)
