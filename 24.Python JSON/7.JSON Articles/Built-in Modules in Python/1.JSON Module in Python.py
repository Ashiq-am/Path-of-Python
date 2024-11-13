import json
data = {
	"name": "Jonny",
	"age": 30,
	"is_student": True,
	"courses": ["Web Dev", "CP"]
}
json_string = json.dumps(data, indent=4)
print(json_string)
