data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 22}]
filtered_data = list(filter(lambda d: d['age'] > 25, data))
print(filtered_data)
