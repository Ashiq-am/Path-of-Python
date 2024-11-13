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

# Using the `update()` Method
new_subjects = {'physics': 88, 'chemistry': 92}
student_data['grades'].update(new_subjects)
print("Using the `update()` Method\n", student_data)
