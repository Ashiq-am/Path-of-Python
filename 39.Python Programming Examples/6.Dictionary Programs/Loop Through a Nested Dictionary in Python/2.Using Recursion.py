def iterate_nested_dict(nested_dict):
	for key, value in nested_dict.items():
		if isinstance(value, dict):
			iterate_nested_dict(value)
		else:
			print(f"Key: {key}, Value: {value}")

nested_dict = {'outer_key': {'inner_key1': 'value1', 'inner_key2': 'value2'}}
iterate_nested_dict(nested_dict)
