def flatten_dict(d):
	flattened_list = []
	for key, value in d.items():
		flattened_list.append(key)
		if isinstance(value, dict):
			flattened_list.extend(flatten_dict(value))
		else:
			flattened_list.append(value)
	return flattened_list

nested_dict = {"a": {"b": "c"}, "d": {"e": "f"}}
flattened_list = flatten_dict(nested_dict)
print(type(nested_dict))
print(flattened_list)
print(type(flattened_list))
