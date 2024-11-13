# Using a loop
nested_dict = {}
keys_hierarchy = ['first_level_key1', 'second_level_key1', 'third_level_key1']
current_dict = nested_dict

for key in keys_hierarchy:
	current_dict = current_dict.setdefault(key, {})

current_dict['final_key'] = 'final_value'

# Example
print(nested_dict['first_level_key1']['second_level_key1']
	['third_level_key1']['final_key'])
