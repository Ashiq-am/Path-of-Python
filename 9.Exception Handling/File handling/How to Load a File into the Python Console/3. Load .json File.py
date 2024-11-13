import json

# Open the JSON file in read mode
with open('a.json', 'r') as file:
	# Load the JSON content into a Python dictionary
	json_content = json.load(file)

# Print the content to the console
print(json_content)
