import json
# age has string value
json_data = '{ "name": "Om Mishra", "age": "22" }'

try:
	data = json.loads(json_data)
	age = int(data["age"])
	print(age)
except ValueError:
	print("'age' value is not a valid integer in JSON data")
