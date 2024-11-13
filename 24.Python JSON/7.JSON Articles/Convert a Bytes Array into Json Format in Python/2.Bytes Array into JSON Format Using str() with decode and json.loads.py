import json

# Sample complex bytes array
bytes_data = b'{"key": "value", "nested": {"inner_key": [1, 2, 3]}}'
print(type(bytes_data))

# Convert bytes to string and parse as JSON
json_data = json.loads(str(bytes_data, 'utf-8'))

# Display the resulting JSON data
print(json_data)
print(type(json_data))
