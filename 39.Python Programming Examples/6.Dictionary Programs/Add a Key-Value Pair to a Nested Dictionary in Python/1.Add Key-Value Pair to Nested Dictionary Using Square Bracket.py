# Original Student Data Dictionary
student_data = {
	'name': 'John Doe',
	'age': 20,
	'grades': {
		'math': 90,
		'english': 85,
		'history': 78
	}
}

print("Original Dictionary\n", student_data)

# Using Square Bracket Notation
student_data['grades']['science'] = 95
print("Using Square Bracket Notation\n", student_data)
