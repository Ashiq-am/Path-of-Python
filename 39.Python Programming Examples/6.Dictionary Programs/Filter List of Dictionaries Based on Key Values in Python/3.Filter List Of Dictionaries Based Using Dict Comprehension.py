data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 22}]
filtered_data = {d['name']: d['age'] for d in data if d['age'] > 25}
print(filtered_data)
