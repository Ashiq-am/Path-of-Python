list_of_dicts = [
	{'name': 'improvement', 'letters': 25, 'city': 'Hyderabad'},
	{'name': 'geeksforgeeks', 'letters': 30, 'city': 'United states'},
	{'name': 'author', 'letters': 22, 'city': 'Japan'}]

key_to_print = 'name'
values = list(map(lambda d: d[key_to_print], filter(lambda d: key_to_print in d, list_of_dicts)))
print(values)
