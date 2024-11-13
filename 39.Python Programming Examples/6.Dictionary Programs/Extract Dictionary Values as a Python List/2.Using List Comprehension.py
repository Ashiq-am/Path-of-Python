list_of_dicts = [
	{'name': 'improvement', 'letters': 25, 'city': 'Hyderabad'},
	{'name': 'geeksforgeeks', 'letters': 30, 'city': 'United states'},
	{'name': 'author', 'letters': 22, 'city': 'Japan'}]

key_to_print = 'city'

values = [d[key_to_print] for d in list_of_dicts if key_to_print in d]
print(values)
