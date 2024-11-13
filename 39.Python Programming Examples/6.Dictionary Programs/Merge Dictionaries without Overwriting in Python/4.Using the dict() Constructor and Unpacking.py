# Sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Using dict() constructor and unpacking
merged_dict = dict(dict1, **dict2)

print(merged_dict)
