import orjson

json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parsing JSON string using orjson.loads()
data = orjson.loads(json_string)

# Displaying the parsed data
print(data)
