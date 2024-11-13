# Using the get() Method
students = {'Math': [85, 90, 78], 'Physics': [92, 88, 95]}

def search_value(dictionary, key, target_value):
	values = dictionary.get(key, [])
	return target_value in values

result = search_value(students, 'Math', 90)
# printing output
print(result)
