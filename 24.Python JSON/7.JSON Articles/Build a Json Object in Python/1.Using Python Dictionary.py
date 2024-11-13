import json

data = {
	"name": "Guru",
	"age": 19,
	"isStudent": True
}

json_string = json.dumps(data)
print(type(json_string))
print(json_string)
