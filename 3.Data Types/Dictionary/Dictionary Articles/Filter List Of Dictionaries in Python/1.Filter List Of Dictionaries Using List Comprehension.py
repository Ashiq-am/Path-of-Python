original_list = [{'name': 'Alice', 'age': 25},
				{'name': 'Bob', 'age': 30},
				{'name': 'Charlie', 'age': 22}]

filtered_list = [d for d in original_list if d['age'] > 25]

print(filtered_list)
