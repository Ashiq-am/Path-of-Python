import json

# Sample list of tuples
list_of_tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

# Define a mapping function
def tuple_to_dict(tpl):
	return {tpl[0]: tpl[1]}

# Convert to JSON string using map and dumps
json_string = json.dumps(list(map(tuple_to_dict, list_of_tuples)))

print(type(list_of_tuples))

# Display the result
print(json_string)

print(type(json_string))
