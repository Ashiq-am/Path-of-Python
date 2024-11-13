from operator import itemgetter

nested_dict = {'a': {'key': 3}, 'b': {'key': 1}, 'c': {'key': 2}}

sorted_dict = dict(
	sorted(nested_dict.items(), key=lambda item: itemgetter('key')(item[1])))

print(sorted_dict)
