import json
# age has string value
json_data = '{ "name": "Om Mishra", "age": "twenty two" }'

try:
	data = json.loads(json_data)
	age = int(data["age"])
	print(age)
except ValueError:
	print("'age' value is not a valid integer in JSON data")
