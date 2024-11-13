def sort_nested_dict(d):
	for key, value in d.items():
		if isinstance(value, dict):
			d[key] = sort_nested_dict(value)
	return dict(sorted(d.items(), key=lambda item: str(item[1]) if not isinstance(item[1], dict) else str(sort_nested_dict(item[1]))))

nested_dict = {'a': {'key': 3}, 'b': {'key': 1},
			'c': {'key': 2, 'inner': {'z': 3, 'x': 1}}}

sorted_dict = sort_nested_dict(nested_dict)
print(sorted_dict)
