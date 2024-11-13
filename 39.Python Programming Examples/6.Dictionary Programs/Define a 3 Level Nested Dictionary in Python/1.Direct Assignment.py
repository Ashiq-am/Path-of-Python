# Direct Assignment
nested_dict = {
	'first_level_key1': {
		'second_level_key1': {
			'third_level_key1': 'value1',
			'third_level_key2': 'value2',
		},
		'second_level_key2': {
			'third_level_key3': 'value3',
			'third_level_key4': 'value4',
		},
	},
	'first_level_key2': {
		'second_level_key3': {
			'third_level_key5': 'value5',
			'third_level_key6': 'value6',
		},
		'second_level_key4': {
			'third_level_key7': 'value7',
			'third_level_key8': 'value8',
		},
	},
}

# Example
print(nested_dict['first_level_key1']['second_level_key1']['third_level_key1'])
