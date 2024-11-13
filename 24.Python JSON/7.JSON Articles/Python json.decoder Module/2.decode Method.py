import json

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Directly decode the JSON string into a Python dictionary
python_obj = json.loads(json_string)

print(python_obj)
