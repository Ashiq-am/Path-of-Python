import json

# Sample nested JSON data
nested_json_data = '{"name": "John", "age": 30, "address": {"city": "New York", "zipcode": "10001"}}'

# Parse JSON data
parsed_data = json.loads(nested_json_data)

# Accessing nested values
name = parsed_data['name']
age = parsed_data['age']
city = parsed_data['address']['city']
zipcode = parsed_data['address']['zipcode']

# Printing the results
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Zipcode: {zipcode}")
