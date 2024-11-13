import json

# Using double quotes in JSON
json_data_fixed = '{"name": "John", "age": 25, "city": "New York"}'
parsed_fixed = json.loads(json_data_fixed)

print("Using double quotes:")
print(parsed_fixed)