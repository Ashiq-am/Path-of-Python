dictionary_lists = {'key1': [1, 2, 3],
					'key2': [4, 5, 6],
					'key3': [7, 8, 9]}

# Using zip and dict constructor
dictionary_sets = dict(
	zip(dictionary_lists.keys(), map(set, dictionary_lists.values())))

print(dictionary_sets)
