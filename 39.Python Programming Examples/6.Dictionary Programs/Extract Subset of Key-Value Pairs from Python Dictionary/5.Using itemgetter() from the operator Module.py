from operator import itemgetter

# initializing dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_extract = {'a', 'b'}

subset_dict = dict(
	zip(keys_to_extract, itemgetter(*keys_to_extract)(original_dict)))

# Printing dictionary
print("Subset dictionary using itemgetter() from the operator Module:", subset_dict)
