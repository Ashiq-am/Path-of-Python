# Original Dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Extract keys, perform slicing, and create a new dictionary
keys = list(original_dict.keys())[1:4]
sliced_dict = {k: original_dict[k] for k in keys}

# Result
print("Original Dictionary:", original_dict)
print("Sliced Dictionary:", sliced_dict)
