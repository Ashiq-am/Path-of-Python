import json

class ListOfListsEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, list):
			return obj
		return json.JSONEncoder.default(self, obj)

# List of lists
data = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

print(type(data))
# Convert into JSON using custom encoder
json_output = json.dumps(data, cls=ListOfListsEncoder)

print(json_output)
print(type(json_output))
