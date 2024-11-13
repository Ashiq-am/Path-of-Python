import json

# Using double quotes in JSON
json_data_double = '{"name": "John", "age": 25, "city": "New York"}'
parsed_double = json.loads(json_data_double)

print("Using double quotes:")
print(parsed_double)
