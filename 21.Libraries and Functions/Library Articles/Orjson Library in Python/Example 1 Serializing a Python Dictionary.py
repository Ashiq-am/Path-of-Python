import orjson

data_to_serialize = {"name": "John", "age": 30, "city": "New York"}

# Serialize the Python dictionary to JSON
json_data = orjson.dumps(data_to_serialize)

print(json_data)
