import json

# Sample list of tuples
list_of_tuples = [(1, 'apple'), (2, 'banana'), (3, 'orange')]

# Convert the list of tuples to a dictionary
dictionary_data = dict(list_of_tuples)

# Convert the dictionary to a JSON string
json_string = json.dumps(dictionary_data)

print(type(list_of_tuples))
print(type(json_string))

# Display the result
print(json_string)
