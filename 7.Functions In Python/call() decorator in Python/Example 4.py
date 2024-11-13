# Defining the decorator function
def call(*argv, **kwargs):
	def call_fn(function):
		return function(*argv, **kwargs)
	return call_fn

# Using the decorator function
@call(6)
def list_of_numbers(n):
	element = []
	for i in range(n):
		element.append(i * 2)
	return element

# Output command
print(len(list_of_numbers),
	list_of_numbers[2])
