# Sample list of dictionaries
list_of_dicts = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}]

# Method 1: Using a Loop
result_string = ''
for dictionary in list_of_dicts:
	for key, value in dictionary.items():
		result_string += f"{key}: {value}, "
result_string = result_string.rstrip(', ')

# Print the result
print(type(list_of_dicts))
print(result_string)
print(type(result_string))
