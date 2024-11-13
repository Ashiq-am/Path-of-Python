from collections import ChainMap

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'd': 3, 'e': 4}
dict2 = {'f': 9, 'c': 6, 'g': 3}

# Merge dictionaries recursively using ChainMap
result = dict(ChainMap(dict1, dict2))
print(result)
