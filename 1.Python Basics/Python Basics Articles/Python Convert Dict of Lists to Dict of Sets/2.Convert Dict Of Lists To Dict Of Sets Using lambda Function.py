dictionary_lists = {'key1': [1, 2, 3],
					'key2': [4, 5, 6],
					'key3': [7, 8, 9]}

# Using map and set
dictionary_sets = dict(
	map(lambda item: (item[0], set(item[1])), dictionary_lists.items()))

print(dictionary_sets)
