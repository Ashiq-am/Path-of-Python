import json

# Example JSON data with bytes
json_data = b'{"name": "Amit", "age": 30, "city": "Delhi"}'

# Decode bytes to string and parse JSON
decoded_data = json_data.decode('utf-8')
parsed_json = json.loads(decoded_data)

# Print parsed JSON
print(parsed_json)
