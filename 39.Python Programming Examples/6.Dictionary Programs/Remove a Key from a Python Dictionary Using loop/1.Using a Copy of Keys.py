my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in list(my_dict.keys()):
	if key == 'b':
		del my_dict[key]

print(my_dict)
