import heapq

nested_dict = {'a': {'value': 5}, 'b': {'value': 3},
			'c': {'value': 8}}

sorted_nested_dict = dict(heapq.nlargest(len(nested_dict), nested_dict.items(),
										key=lambda x: x[1]['value']))

print(sorted_nested_dict)
