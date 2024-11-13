import json

# Example JSON data with bytes
json_data = b'{"name": "Ankit", "age": 30, "city": "Mumbai"}'

# Decode bytes to string and parse JSON
decoded_data = json_data.decode('utf-8')
parsed_json = json.loads(decoded_data)

# Accessing values from parsed JSON
name = parsed_json['name']
age = parsed_json['age']
city = parsed_json['city']

# Printing parsed values
print("Name:", name)
print("Age:", age)
print("City:", city)
