# Original set
my_set = {1, 2, 3}
my_dict = {'a': 4, 'b': 5, 'c': 6}
my_dict_as_set = set(my_dict.items())

# Using union method
my_set = my_set.union(my_dict_as_set)
print(f"Set after adding the dictionary: {my_set}")
