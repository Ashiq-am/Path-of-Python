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

# Using the `setdefault()` Method
student_data.setdefault('grades', {})['biology'] = 89
print("Using the `setdefault()` Method\n", student_data)
