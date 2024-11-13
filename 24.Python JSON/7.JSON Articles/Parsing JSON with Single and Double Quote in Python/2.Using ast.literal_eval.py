import ast

json_data = '{"name": "John", \'age\': 30, "city": \'New York\'}'

# Parsing JSON with mixed quotes using ast.literal_eval
parsed_data = ast.literal_eval(json_data)

# Accessing parsed data
print(parsed_data['name'])
print(parsed_data['age'])
print(parsed_data['city'])
