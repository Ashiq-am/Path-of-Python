# Import Module
import json

# Create geeks function


def geeks():

	# Create Dictionary
	value = {
		"firstName": "Pawan",
		"lastName": "Gupta",
		"hobbies": ["playing", "problem solving", "coding"],
		"age": 20,
		"children": [
			{
				"firstName": "mohan",
				"lastName": "bansal",
				"age": 15
			},
			{
				"firstName": "prerna",
				"lastName": "Doe",
				"age": 18
			}
		]
	}

	# Dictionary to JSON Object using dumps() method
	# Return JSON Object
	return json.dumps(value)


# Call Function and Print it.
print(geeks())
