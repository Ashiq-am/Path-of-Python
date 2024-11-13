import json

# Sample list of dictionaries
list_of_dicts = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}]
result_string = json.dumps(list_of_dicts, indent=2)

# Print the result
print(type(list_of_dicts))
print(result_string)
print(type(result_string))
