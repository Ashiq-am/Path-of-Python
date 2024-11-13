import json

# Using Recursive Function
def iterate_nested_json_recursive(json_obj):
	for key, value in json_obj.items():
		if isinstance(value, dict):
			iterate_nested_json_recursive(value)
		else:
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

print("\nUsing Recursive Function")
iterate_nested_json_recursive(nested_json)
