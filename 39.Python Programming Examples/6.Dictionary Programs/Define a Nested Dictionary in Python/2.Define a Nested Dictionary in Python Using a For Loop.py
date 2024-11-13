outer_keys = ['outer_key1', 'outer_key2']
inner_keys = ['inner_key1', 'inner_key2']

nested_dict = {outer_key: {inner_key: f'value_{outer_key}_{inner_key}'
						for inner_key in inner_keys}
			for outer_key in outer_keys}

print(nested_dict)
