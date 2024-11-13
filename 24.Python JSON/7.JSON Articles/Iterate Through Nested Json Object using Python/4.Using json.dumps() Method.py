import json

# Using json.loads with json.dumps
def iterate_nested_json_flatten(json_obj):
	flattened_json_str = json.dumps(json_obj)
	flattened_json = json.loads(flattened_json_str)

	for key, value in flattened_json.items():
		print(f"{key}: {value}")

# Example usage with a nested JSON object
nested_json = {
	"name": "John",
	"age": 30,
	"address": {
		"city": "New York",
		"zip": "10001"
	}
}

print("\nUsing json.dumps")
iterate_nested_json_flatten(nested_json)
