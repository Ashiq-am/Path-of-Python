def custom_filter(item):
	return item['age'] > 25 and item['city'] == 'New York'

data = [
	{'name': 'Alice', 'age': 25, 'city': 'New York'},
	{'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
	{'name': 'Charlie', 'age': 28, 'city': 'New York'},
	# ... additional dictionaries ...
]

filtered_data = list(filter(custom_filter, data))
print(filtered_data)
