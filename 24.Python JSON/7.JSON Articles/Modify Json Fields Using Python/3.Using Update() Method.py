import json

# Sample JSON data
json_data = '{"name": "Eva", "age": 28, "city": "Seattle"}'

# Parse the JSON data and convert it to a dictionary
data = json.loads(json_data)

# Modify the 'name' field
data.update({"name": "Sophia"})

# Convert the modified data back to JSON
modified_json = json.dumps(data)

print('Before Modifying:', json_data)
print('After Modifying:', modified_json)