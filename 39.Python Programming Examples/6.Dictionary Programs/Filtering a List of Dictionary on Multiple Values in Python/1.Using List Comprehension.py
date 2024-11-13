data = [
	{'name': 'Alice', 'age': 25, 'city': 'New York'},
	{'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
	{'name': 'Charlie', 'age': 28, 'city': 'New York'},
	# ... additional dictionaries ...
]

filtered_data = [item for item in data if item['age'] > 25 and item['city'] == 'New York']
print(filtered_data)
