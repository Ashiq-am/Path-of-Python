import json

# load JSON data from file
with open('input.json', 'r') as file:
	data = json.load(file)

# key to remove
key_to_remove = "featured_article"

# checking if the key exists before removing
if key_to_remove in data:
	removed_value = data.pop(key_to_remove)
	print(f"Removed key '{key_to_remove}' with value: {removed_value}")

# saving the updated JSON data back to the file
with open('output.json', 'w') as file:
	json.dump(data, file, indent=2)
