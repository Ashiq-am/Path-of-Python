# Using List Comprehension
def iterate_nested_json_list_comprehension(json_obj):
	items = [(key, value) if not isinstance(value, dict) else (key, iterate_nested_json_list_comprehension(value)) for key, value in json_obj.items()]
	return items

# Example usage with a nested JSON object
nested_json = {
	"name": "John",
	"age": 30,
	"address": {
		"city": "New York",
		"zip": "10001"
	}
}

print("\nUsing List Comprehension")
result = iterate_nested_json_list_comprehension(nested_json)
print(result)
