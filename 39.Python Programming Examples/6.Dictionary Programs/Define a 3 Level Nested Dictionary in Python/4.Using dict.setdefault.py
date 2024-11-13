# Using dict.setdefault
nested_dict = {}
nested_dict.setdefault('first_level_key1', {}).setdefault(
	'second_level_key1', {})['third_level_key1'] = 'value1'

# Example
print(nested_dict['first_level_key1']['second_level_key1']['third_level_key1'])
