import orjson

# Nested JSON string
json_string = '{"person": {"name": "Alice", "age": 25, "city": "London"}}'

# Parsing nested JSON string
data = orjson.loads(json_string)

# Accessing nested data
print("Name:", data['person']['name'])
print("Age:", data['person']['age'])
print("City:", data['person']['city'])
