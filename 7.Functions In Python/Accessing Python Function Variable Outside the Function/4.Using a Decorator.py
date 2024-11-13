def store_variable(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		wrapper.variable = result
		return result
	return wrapper

@store_variable
def get_variable():
	return 42

# Accessing the variable through the decorated function
get_variable()
print(get_variable.variable)
