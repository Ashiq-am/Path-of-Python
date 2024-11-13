import json

# Sample JSON array
people_data = '[{"name": "John", "age": 30}, {"name": "Alice", "age": 25}, {"name": "Bob", "age": 35}]'
people = json.loads(people_data)

# Filtering by value
filtered_people = [person for person in people if person["age"] > 30]
print(filtered_people)
