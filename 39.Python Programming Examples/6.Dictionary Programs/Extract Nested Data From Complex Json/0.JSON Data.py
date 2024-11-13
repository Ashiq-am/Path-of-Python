import json

# Complex dictionary with nested structures
data = {
	"location": {
		"country": "India",
		"state": "Uttar Pradesh",
		"city": "Greater Noida"
	},
	"organizations": [
		{
			"name": "GeeksforGeeks",
			"type": "Educational",
			"departments": ["Computer Science", "Mathematics", "Physics"]
		},
		{
			"name": "TechCorp",
			"type": "Technology",
			"departments": ["Software Development", "Hardware Design"]
		}
	],
	"projects": {
		"ongoing": ["ProjectA", "ProjectB"],
		"completed": ["ProjectX", "ProjectY"]
	}
}

# Convert dictionary to JSON with indentation for readability
json_data = json.dumps(data, indent=2)
