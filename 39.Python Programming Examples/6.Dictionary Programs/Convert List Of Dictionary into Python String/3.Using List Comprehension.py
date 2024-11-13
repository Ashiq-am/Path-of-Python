# Sample list of dictionaries
list_of_dicts = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}]

result_list = [', '.join([f"{key}: {value}" for key, value in dictionary.items()]) for dictionary in list_of_dicts]
result_string = ', '.join(result_list)

# Print the result
print(type(list_of_dicts))
print(result_string)
print(type(result_string))
