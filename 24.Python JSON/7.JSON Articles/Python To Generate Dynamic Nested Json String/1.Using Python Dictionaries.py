import json

# Using Python Dictionaries
data_dict = {
	"name": "John",
	"age": 25,
	"address": {"city": "Cityville", "zip": "12345"},
	"contacts": [{"type": "email", "value": "john@example.com"}]
}

json_string_dict = json.dumps(data_dict, indent=2)
print("Output")
print(json_string_dict)
