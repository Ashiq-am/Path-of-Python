import json

json_data = '{"name": "Alice", "age": 30, "city": "New York"}'

# Using JSONDecoder to parse JSON
decoder = json.JSONDecoder()
python_obj = decoder.decode(json_data)

print(python_obj)
