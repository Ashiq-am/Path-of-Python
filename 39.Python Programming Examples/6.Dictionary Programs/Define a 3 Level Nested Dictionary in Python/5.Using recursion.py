# Using recursion
def add_nested_key(dictionary, keys, value):
	if len(keys) == 1:
		dictionary[keys[0]] = value
	else:
		add_nested_key(dictionary.setdefault(keys[0], {}), keys[1:], value)


nested_dict = {}
add_nested_key(nested_dict, ['first_level_key1',
							'second_level_key1', 'third_level_key1'], 'value1')

# Example
print(nested_dict['first_level_key1']['second_level_key1']['third_level_key1'])
