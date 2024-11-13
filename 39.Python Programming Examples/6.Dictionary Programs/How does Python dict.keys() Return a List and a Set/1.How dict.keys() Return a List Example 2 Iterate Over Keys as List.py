# Creating a sample dictionary
sample_dict = {'a': 1, 'b': 2, 'c': 3}

# Obtaining keys using dict.keys()
keys_view = sample_dict.keys()

# Iterating over keys
for key in keys_view:
	print("Key:", key)

# Converting keys to a list
keys_list = list(keys_view)

# Displaying the list
print(type(keys_view))
print("Keys as List:", keys_list)
print(type(keys_list))
