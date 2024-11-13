list_of_dicts = [
	{'name': 'improvement', 'letters': 25, 'city': 'Hyderabad'},
	{'name': 'geeksforgeeks', 'letters': 30, 'city': 'United states'},
	{'name': 'author', 'letters': 22, 'city': 'Japan'}]

selected_key = 'city'

selected_pairs = list(map(lambda d: {selected_key: d[selected_key]}, list_of_dicts))
print(selected_pairs)
