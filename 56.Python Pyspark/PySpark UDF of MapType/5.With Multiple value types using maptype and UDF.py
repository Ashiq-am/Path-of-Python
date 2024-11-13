# pyspark program to describe maptype with mixed value types
def process_map(map_data):
	# Process integer value
	integer_value = map_data.get('integer')
	if integer_value is not None:
		# Perform some operation on the integer value
		map_data['integer'] = integer_value * 2

	# Process array value
	array_value = map_data.get('array')
	if array_value is not None and isinstance(array_value, list):
		# Perform some operation on each element of the array
		map_data['array'] = [element.upper() for element in array_value]

	# Process string value
	string_value = map_data.get('string')
	if string_value is not None and isinstance(string_value, str):
		# Perform some operation on the string value
		map_data['string'] = string_value.lower()

	return map_data

my_map = {
	'integer': 10,
	'array': ['apple', 'banana', 'cherry'],
	'string': 'Hello World'
}

# calling the function
processed_map = process_map(my_map)

# printing the result
print(processed_map)
