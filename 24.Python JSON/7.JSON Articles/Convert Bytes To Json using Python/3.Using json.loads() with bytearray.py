import json

# Complex byte data
byte_data = b'{"name": "John", "age": 30, "city": "New York", "skills": ["Python", "JavaScript"]}'

json_data_4 = json.loads(bytearray(byte_data))
print(json_data_4)
