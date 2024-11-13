import json

# JSON string representing an array of objects
json_string = '''
[
    {"name": "tom", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "San Francisco"},
    {"name": "Doe", "age": 22, "city": "Chicago"}
]
'''

try:
    # Decode the JSON string into a Python list of dictionaries
    python_list = json.loads(json_string)
    print("Valid JSON:", python_list)
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)
