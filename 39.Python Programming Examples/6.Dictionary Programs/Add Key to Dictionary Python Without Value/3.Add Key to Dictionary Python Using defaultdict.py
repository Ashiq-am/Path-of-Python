from collections import defaultdict

# Using defaultdict
my_dict = defaultdict(lambda: None)
key = 'new_key'

# Adding a key without a value
my_dict[key]

# Displaying the dictionary
print(dict(my_dict))
