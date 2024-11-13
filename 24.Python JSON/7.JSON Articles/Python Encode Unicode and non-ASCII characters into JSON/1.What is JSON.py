import json

# Define a dictionary
my_dict = {
	"name": "John Doe",
	"age": 35,
	"email": "john.doe@example.com"
}

# Use the json.dumps() method to encode
# the dictionary as a JSON string
json_str = json.dumps(my_dict)

# Print the JSON string
print(json_str)
