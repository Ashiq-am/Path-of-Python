import json

# JSON string with an array of objects and nested structures
json_string = '''
{
    "company": "TechCorp",
    "employees": [
        {
            "name": "Alice",
            "age": 28,
            "position": "Engineer",
            "skills": ["Python", "JavaScript", "SQL"]
        },
        {
            "name": "Bob",
            "age": 34,
            "position": "Manager",
            "skills": ["Leadership", "Communication", "Planning"]
        }
    ],
    "location": {
        "city": "San Francisco",
        "state": "CA",
        "country": "USA"
    }
}
'''

# Decode the JSON string into a Python dictionary
python_obj = json.loads(json_string)

# Print the resulting Python dictionary
print(python_obj)
