# Original dictionary
my_dict = {'gfg': 3, 'geeks': 5, 'for': 2, 'geek': 4, 'tutorial': 8}

# Key to be removed
key_to_remove = 'geek'

# Using del method
if key_to_remove in my_dict:
	del my_dict[key_to_remove]
	print(f"Key '{key_to_remove}' removed. Dictionary after removal: {my_dict}")
else:
	print(f"Key '{key_to_remove}' not found in the dictionary.")
