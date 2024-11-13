list_of_dicts = [
	{'name': 'improvement', 'letters': 25, 'city': 'Hyderabad'},
	{'name': 'geeksforgeeks', 'letters': 30, 'city': 'United states'},
	{'name': 'author', 'letters': 22, 'city': 'Japan'}]

key_to_print = 'name'

ans = []
# iterated the list of dictionary
for d in list_of_dicts:
	if key_to_print in d:
		ans.append(d[key_to_print])

print(ans)
