from collections import defaultdict

my_dict = defaultdict(int, {'a': 1, 'b': 2})

# Adding a new value to an existing key using defaultdict
my_dict['a'] = 3

print("defaultdict Class:", dict(my_dict))
