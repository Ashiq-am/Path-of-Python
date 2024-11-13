# Import required libraries
import json

data = [{"studentid": 1, "name": "ABC", "subjects": ["Python", "Data Structures"]},
		{"studentid": 2, "name": "PQR", "subjects": ["Java", "Operating System"]}]

# Write pretty print JSON data to file
with open("filename.json", "w") as write_file:
	json.dump(data, write_file, indent=4)
