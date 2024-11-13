import json
s = '{"name": "Ram", "age": 22, "city": "India"}'

data = json.loads(s)

print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])
