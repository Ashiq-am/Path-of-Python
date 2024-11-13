import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Parsing JSON with mixed quotes using json.loads
parsed_data = json.loads(json_data, strict=False)

# Accessing parsed data
print(parsed_data['name'])
print(parsed_data['age'])
print(parsed_data['city'])
