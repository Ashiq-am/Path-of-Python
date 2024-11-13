import json

# load JSON data from file
with open('input.json', 'r') as file:
    data = json.load(file)

# key to remove
key_to_remove = "featured_article"

# check if key exists
if key_to_remove in data.keys():

    removed_value = data[key_to_remove]

    # Removing the key
    del data[key_to_remove]

    print(f"Removed key '{key_to_remove}' with value: {removed_value}")

else:
    print("Key does not exist")

# Write the updated json to json file
with open('output.json', 'w') as f:
    # write updated data
    json.dump(data, f, indent=2)
