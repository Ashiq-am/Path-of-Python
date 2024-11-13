original_list = [{'name': 'Alice', 'age': 25},
				{'name': 'Bob', 'age': 30},
				{'name': 'Charlie', 'age': 22}]

filtered_list = list(filter(lambda d: d['age'] > 25, original_list))

print(filtered_list)
