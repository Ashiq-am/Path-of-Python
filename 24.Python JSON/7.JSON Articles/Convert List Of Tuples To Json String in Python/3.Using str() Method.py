import json

# Another sample list of tuples with mixed data types
list_of_tuples = [('a', 1), (2, 'b'), ('c', True)]

# Convert the list of tuples to a dictionary, ensuring both keys and values are strings
mixed_dictionary_data = {str(key): str(value) for key, value in list_of_tuples}

# Convert the dictionary to a JSON string
json_string = json.dumps(mixed_dictionary_data)

print(type(list_of_tuples))
print(type(json_string))

# Display the result
print(json_string)
