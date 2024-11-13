data = [
	{'name': 'Alice', 'age': 25, 'city': 'New York'},
	{'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
	{'name': 'Charlie', 'age': 28, 'city': 'New York'},
	# ... additional dictionaries ...
]

filtered_data = list(filter(lambda x: x['age'] > 25 and x['city'] == 'New York', data))
print(filtered_data)
