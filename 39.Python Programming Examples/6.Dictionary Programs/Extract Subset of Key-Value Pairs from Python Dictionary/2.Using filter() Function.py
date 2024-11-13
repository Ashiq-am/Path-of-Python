original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using filter() to get an iterable of key-value pairs based on the condition
subset_items = filter(lambda item: item[0] in {
					'a', 'b'}, original_dict.items())

# Converting the iterable back to a dictionary
subset_dict = dict(subset_items)
print("Subset dictionary using filter() Function:", subset_dict)
