# Original dictionary of lists
dictionary_lists = {'key1': [1, 2, 3],
					'key2': [4, 5, 6],
					'key3': [7, 8, 9]}

# Converting dictionary of lists to dictionary of sets
dictionary_sets = {key: set(value) for key, value in dictionary_lists.items()}

# Display the result
print(dictionary_sets)
