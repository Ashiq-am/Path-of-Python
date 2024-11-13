import yaml

# Serialize
data = {'name': 'John', 'age': 30}
with open('data.yaml', 'w') as file:
    yaml.dump(data, file)

# Deserialize
with open('data.yaml', 'r') as file:
    serialized_data = file.read()
    file.seek(0)
    loaded_data = yaml.safe_load(file)

print("Type of serialized data:", type(serialized_data))
print("Deserialized data:", loaded_data)
print("Type of deserialized data:", type(loaded_data))
