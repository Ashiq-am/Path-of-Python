import json

# Sample JSON data
json_data = """
[
	{"id": 1, "name": "John"},
	{"id": 2, "name": "Jane"},
	{"id": 3, "name": "Bob"}
]
"""

# Convert JSON data to a Python object
data = json.loads(json_data)

# Iterate through the JSON array
for item in data:
	print(item["id"], item["name"])
