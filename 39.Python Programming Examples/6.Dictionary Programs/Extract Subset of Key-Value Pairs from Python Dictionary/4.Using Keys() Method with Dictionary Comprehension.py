# initializing dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_extract = {'a', 'b'}

# Creating a new dictionary with only key-value pairs where the key is in keys_to_extract
subset_dict = {key: original_dict[key]
			for key in original_dict.keys() & keys_to_extract}

# Printing dictionary
print("Subset dictionary using Keys() Method with Dictionary Comprehension:", subset_dict)
