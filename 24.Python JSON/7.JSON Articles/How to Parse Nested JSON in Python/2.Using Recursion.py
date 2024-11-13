import json

# Sample nested JSON data
nested_json_data = '{"person": {"name": "John", "age": 30, "address": {"city": "New York", "zipcode": "10001"}}}'

def parse_json(data):
	result = {}
	for key, value in data.items():
		if isinstance(value, dict):
			result[key] = parse_json(value)
		else:
			result[key] = value
	return result

# Parsing JSON data using recursion
parsed_data = parse_json(json.loads(nested_json_data))

# Accessing nested values
name = parsed_data['person']['name']
age = parsed_data['person']['age']
city = parsed_data['person']['address']['city']
zipcode = parsed_data['person']['address']['zipcode']

# Printing the results
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Zipcode: {zipcode}")
