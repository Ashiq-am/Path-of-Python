# Using defaultdict from collections
from collections import defaultdict

students = defaultdict(list)
students['Math'].extend([85, 90, 78])
students['Physics'].extend([92, 88, 95])

def search_value(dictionary, key, target_value):
	if key in dictionary:
		values = dictionary[key]
		if target_value in values:
			return True
	return False

# printing output
result = search_value(students, 'Math', 90)
print(result)
