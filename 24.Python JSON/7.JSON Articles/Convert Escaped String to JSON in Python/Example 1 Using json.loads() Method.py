import json
import ast

escaped_string = '{"name": "John\\nDoe", "age": 25}'

# Parse the escaped string using ast.literal_eval()
unescaped_dict = ast.literal_eval(escaped_string)

# Convert the dictionary to JSON using json.dumps()
json_data = json.dumps(unescaped_dict)

print(json_data)
