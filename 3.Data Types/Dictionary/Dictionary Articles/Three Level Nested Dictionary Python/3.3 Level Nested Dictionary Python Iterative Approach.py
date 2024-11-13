nested_dict = {}
levels = ['first_level_key', 'second_level_key', 'third_level_key']

current_dict = nested_dict
for level in levels:
	current_dict[level] = {}
	current_dict = current_dict[level]

current_dict['final_key'] = 'value'
print(nested_dict)
