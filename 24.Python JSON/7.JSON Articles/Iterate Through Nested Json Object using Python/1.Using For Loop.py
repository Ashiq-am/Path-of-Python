# Using For Loop
def iterate_nested_json_for_loop(json_obj):
	for key, value in json_obj.items():
		if isinstance(value, dict):
			iterate_nested_json_for_loop(value)
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

print("Using For Loop")
iterate_nested_json_for_loop(nested_json)
