def get_data(condition):
	"""
	This function is expected to return a list or tuple,
	but under certain conditions, it returns an integer.
	"""
	if condition:
		return [1, 2, 3] # Returns a list
	else:
		return 42 # Returns an integer

# Function call with a condition that leads to an integer being returned
result = get_data(False)

# Attempting to index the result, which is an integer in this case
first_element = result[0]
