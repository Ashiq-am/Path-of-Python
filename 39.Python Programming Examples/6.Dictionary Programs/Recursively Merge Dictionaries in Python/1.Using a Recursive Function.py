def recursive_merge(dict1, dict2):
	for key, value in dict2.items():
		if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
			# Recursively merge nested dictionaries
			dict1[key] = recursive_merge(dict1[key], value)
		else:
			# Merge non-dictionary values
			dict1[key] = value
	return dict1

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'd': 3, 'e': 4}
dict2 = {'f': 9, 'c': 6, 'g': 3}

# Merge dictionaries recursively
result = recursive_merge(dict1, dict2)
print(result)
