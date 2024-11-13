import json

# Load the JSON data
with open("data.json") as f:
	data = json.load(f)

# Iterate through the JSON array
for item in data:
	print(item["id"], item["name"])
