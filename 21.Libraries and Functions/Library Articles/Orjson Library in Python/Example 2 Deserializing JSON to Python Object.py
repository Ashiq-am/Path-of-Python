import orjson

json_data = b'{"name":"Jane","age":25,"city":"Los Angeles"}'

# Deserialize JSON to Python dictionary
python_object = orjson.loads(json_data)

print(python_object)
