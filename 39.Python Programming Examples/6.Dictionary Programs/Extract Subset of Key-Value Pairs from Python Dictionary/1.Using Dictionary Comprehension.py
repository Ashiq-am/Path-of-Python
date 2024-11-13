# initializing dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Creating a new dictionary with only key-value pairs where the key is in {'a', 'b'}
subset_dict = {key: value for key, value in original_dict.items() if key in {
	'a', 'b'}}
# Printing dictionary
print("Subset dictionary using Dictionary Comprehension:", subset_dict)
