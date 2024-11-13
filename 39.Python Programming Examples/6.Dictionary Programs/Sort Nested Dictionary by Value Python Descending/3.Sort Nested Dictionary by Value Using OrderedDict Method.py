from collections import OrderedDict

nested_dict = {'a': {'value': 5}, 'b': {'value': 3},
			'c': {'value': 8}}

sorted_nested_dict = OrderedDict(sorted(nested_dict.items(),
										key=lambda x: x[1]['value'],
										reverse=True))

final_dict = dict(sorted_nested_dict)
print(final_dict)
