# Python program to convert
# Python to JSON


import json

# Data to be written
dictionary = {
	"name": "sunil",
	"depatment": "HR",
	"Company": 'GFG'
}

# Serializing json
json_object = json.dumps(dictionary)
print(json_object)
