def deepcopy_dict(d):
	new_dict = {}
	for key, value in d.items():
		if isinstance(value, dict):
			new_dict[key] = deepcopy_dict(value)
		else:
			new_dict[key] = value
	return new_dict

# Original dictionary
original_dict = {'title': 'GeeksforGeeks',
				'website': {'category': 'Computer Science'}}

# Deep copy using recursion
copied_dict = deepcopy_dict(original_dict)

# Modify the copied_dict to demonstrate deep copying
copied_dict['website']['category'] = 'Programming'

# Output
print("Original Dictionary:")
print(original_dict)
print("Copied Dictionary:")
print(copied_dict)
