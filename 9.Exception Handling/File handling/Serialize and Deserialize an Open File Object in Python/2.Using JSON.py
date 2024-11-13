import json

# Serialize
data = {'name': 'John', 'age': 30}
with open('data.json', 'w') as file:
    json.dump(data, file)

# Deserialize
with open('data.json', 'r') as file:
    serialized_data = file.read()
    file.seek(0)
    loaded_data = json.load(file)

print("Type of serialized data:", type(serialized_data))
print("\nDeserialized data:", loaded_data)
print("Type of deserialized data:", type(loaded_data))
