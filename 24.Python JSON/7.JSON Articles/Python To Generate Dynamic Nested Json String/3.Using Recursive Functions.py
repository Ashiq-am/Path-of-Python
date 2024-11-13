import json

# Using Recursive Functions
def convert_to_json(obj):
	if isinstance(obj, dict):
		return {key: convert_to_json(value) for key, value in obj.items()}
	elif isinstance(obj, list):
		return [convert_to_json(item) for item in obj]
	else:
		return obj

data_recursive = {
	"name": "Alice",
	"age": 28,
	"address": {"city": "Villagetown", "zip": "67890"},
	"contacts": [{"type": "email", "value": "alice@example.com"}]
}

json_string_recursive = json.dumps(convert_to_json(data_recursive), indent=2)
print("\nMethod 3:")
print(json_string_recursive)
