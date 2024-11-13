import json

# Using double quotes with escape characters in JSON
json_data_escape_double = '{"message": "Hello, \\"World\\"!"}'
parsed_escape_double = json.loads(json_data_escape_double)

print("\nUsing double quotes with escape characters:")
print(parsed_escape_double)
