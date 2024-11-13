import json

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Create a JSONDecoder object
decoder = json.JSONDecoder()

# Decode the JSON string into a Python dictionary
python_obj = decoder.decode(json_string)

print(python_obj)
