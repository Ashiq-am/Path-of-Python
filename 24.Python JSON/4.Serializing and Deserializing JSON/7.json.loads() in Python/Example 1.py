import json

# JSON string:
# Multi-line string
x = """{ 
	"Name": "Jennifer Smith", 
	"Contact Number": 7867567898, 
	"Email": "jen123@gmail.com", 
	"Hobbies":["Reading", "Sketching", "Horse Riding"] 
	}"""

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
