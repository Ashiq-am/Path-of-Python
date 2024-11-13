from itertools import chain

nested_dict = {'outer_key': {'inner_key1': 'value1', 'inner_key2': 'value2'}}

for key, value in chain.from_iterable(nested_dict.items()):
	print(f"Key: {key}, Value: {value}")
