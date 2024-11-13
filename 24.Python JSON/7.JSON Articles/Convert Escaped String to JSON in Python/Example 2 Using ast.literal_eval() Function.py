import json

def custom_decoder(obj):
	# Replace escape sequences in string values
	for key, value in obj.items():
		if isinstance(value, str):
			obj[key] = value.replace("\\n", "\n").replace("\\t", "\t")
	return obj

escaped_string = '{"name": "John\\nDoe", "age": 25}'

# Use json.loads() with the custom object_hook
json_data = json.loads(escaped_string, object_hook=custom_decoder)

print(json_data)
