from operator import itemgetter

nested_dict = {'a': {'value': 5}, 'b': {'value': 3},
			'c': {'value': 8}}

sorted_nested_dict = dict(sorted(nested_dict.items(),
								key=lambda x: itemgetter('value')(x[1]),
								reverse=True))

print(sorted_nested_dict)
