import orjson

# Invalid JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"'

try:
    # Parsing invalid JSON string
    data = orjson.loads(json_string)
    print(data)
except orjson.JSONDecodeError as e:
    print("Error parsing JSON:", e)
