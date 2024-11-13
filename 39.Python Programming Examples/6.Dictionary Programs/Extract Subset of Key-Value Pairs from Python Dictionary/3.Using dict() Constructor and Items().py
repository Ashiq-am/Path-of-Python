# initializing dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Creating a dictionary directly using the dict() constructor and a comprehension
subset_dict = dict((key, original_dict[key])
				for key in {'a', 'b'} if key in original_dict)

# Printing dictionary
print("Subset dictionary using dict() Constructor and Items():", subset_dict)
