# code
import json

# Using single quotes in JSON
json_data_single = "{'name': 'John', 'age': 25, 'city': 'New York'}"
parsed_single = json.loads(json_data_single)

print("Using single quotes:")
print(parsed_single)