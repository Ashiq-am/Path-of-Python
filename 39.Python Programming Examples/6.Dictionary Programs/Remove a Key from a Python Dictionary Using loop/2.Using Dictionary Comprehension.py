my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict = {key: value for key, value in my_dict.items() if key != 'b'}

print(my_dict)
