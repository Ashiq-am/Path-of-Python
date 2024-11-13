import re
import json


def custom_json_parser(json_data):
	# Replace single quotes with double quotes
	json_data = re.sub(r"\'", '"', json_data)

	# Use json.loads for parsing
	parsed_data = json.loads(json_data)

	return parsed_data


json_data = '{"name": "John", \'age\': 30, "city": \'New York\'}'

# Parsing JSON with mixed quotes using a custom parser
parsed_data = custom_json_parser(json_data)

# Accessing parsed data
print(parsed_data['name'])
print(parsed_data['age'])
print(parsed_data['city'])
