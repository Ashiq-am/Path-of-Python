# Using a List as the Value
students = {'Math': [85, 90, 78], 'Physics': [92, 88, 95]}

def search_value(dictionary, key, target_value):
	if key in dictionary:
		values = dictionary[key]
		if target_value in values:
			return True
	return False

# printing output
result = search_value(students, 'Math', 90)
print(result)
