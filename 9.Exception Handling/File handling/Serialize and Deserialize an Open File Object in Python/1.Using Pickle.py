import pickle

# Serialize
data = {'name': 'John', 'age': 30}
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Deserialize
with open('data.pickle', 'rb') as file:
    serialized_data = file.read()
    file.seek(0)
    loaded_data = pickle.load(file)

print("Type of serialized data:", type(serialized_data))
print("\nDeserialized data:", loaded_data)
print("Type of deserialized data:", type(loaded_data))
