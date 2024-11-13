# Import required libraries
import json

# Read JSON data from file and pretty print it
with open("filename.json", "r") as read_file:
	# Convert JSON file to Python Types
	obj = json.load(read_file)

	# Pretty print JSON data
	pretty_json = json.dumps(obj, indent=4)
	print(pretty_json)
