from collections import ChainMap

# Sample dictionaries
dict1 = {'a': 1, 'e': 2}
dict2 = {'b': 3, 'c': 4}

# Using ChainMap
merged_dict = dict(ChainMap(dict1, dict2))

print(merged_dict)
