import json

# Define a dictionary using a mix of single and double quotes
mixed_quotes_data = {
	'name': "John",
	"age": 30,
	'city': 'New York',
	"is_student": False,
	"grades": {
		"math": 95,
		'history': 87,
		"english": 92
	}
}

# Convert the dictionary to a JSON-formatted string
json_data = json.dumps(mixed_quotes_data, indent=2)

# Print the JSON-formatted string
print(json_data)
