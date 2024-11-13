nested_dict = {'outer_key': {'inner_key1': 'value1', 'inner_key2': 'value2'}}

for outer_key, inner_dict in nested_dict.items():
	print(f"Outer Key: {outer_key}")
	for inner_key, value in inner_dict.items():
		print(f"Inner Key: {inner_key}, Value: {value}")
