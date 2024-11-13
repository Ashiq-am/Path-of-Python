nested_dict = {'a': {'key': 3}, 'b': {'key': 1}, 'c': {'key': 2}}

sorted_dict = dict(
	sorted(nested_dict.items(), key=lambda item: item[1]['key']))

print(sorted_dict)
