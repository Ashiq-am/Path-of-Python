import json

# Using single quotes in JSON
json_data_single = "{'name': 'John', 'age': 25, 'city': 'New York'}"
parsed_single = json.loads(json_data_single.replace("'", "\""))

print("\nUsing single quotes:")
print(parsed_single)
