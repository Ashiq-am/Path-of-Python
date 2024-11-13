import json

# Sample JSON data
json_data = '{"name": "John", "age": 25, "city": "New York"}'
data = json.loads(json_data)

# Modify the 'age' field
data['age'] = 26

# Convert the modified data back to JSON
modified_json = json.dumps(data)

print('Before Modifying:', json_data)
print('After Modifying:', modified_json)