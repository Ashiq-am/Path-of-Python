import json
# JSON does not contain key "city"

json_data = '{ "name": "Om Mishra", "age": 22 }'
try:
	data = json.loads(json_data)
	city = data["name"]
	print(city)
except KeyError:
	print("Missing 'city' key in JSON data")
