my_dict = {'a': 1, 'b': 2}

# Add 3 to the value of key 'a', use 0 if 'a' doesn't exist
my_dict['a'] = my_dict.get('a', 0) + 3
print(my_dict)
