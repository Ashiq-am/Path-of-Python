import json

data = {
	"Name": {
		"0": "Harsha",
		"1": "Vardhan",
		"2": "Krishna",
		"3": "Hanuman",
		"4": "Shiva"
	},
	"Roll_no": {
		"0": 1,
		"1": 2,
		"2": 3,
		"3": 4,
		"4": 5
	},
	"subject": {
		"0": "C",
		"1": "JAVA",
		"2": "C++",
		"3": "SWIFT",
		"4": "PYTHON"
	}
}

with open('subject.json', 'w') as json_file:
	json.dump(data, json_file, indent=4)
