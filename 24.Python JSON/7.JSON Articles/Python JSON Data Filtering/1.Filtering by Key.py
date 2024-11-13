import json

# Sample JSON data
person_data = '{"name": "John", "age": 30, "city": "New York", "occupation": "Engineer"}'
person = json.loads(person_data)

# Filtering by key
filtered_data = {key: person[key] for key in ["name", "age"]}
print(filtered_data)
