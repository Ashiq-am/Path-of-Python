import json

# Complex byte data
byte_data = b'{"name": "John", "age": 30, "city": "New York", "skills": ["Python", "JavaScript"]}'

json_data_2 = json.loads(str(byte_data, 'utf-8'))
print(json_data_2)
