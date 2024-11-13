import json

# Remove the extra comma and use double quotes in JSON
json_data_fixed = '{"name": "John", "age": 25, "city": "New York"}'
parsed_fixed = json.loads(json_data_fixed)

print("Using double quotes and fixing the comma:")
print(parsed_fixed)