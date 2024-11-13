# Example Dictionary
my_dict = {'outer': {'inner': 'value'}}

# Using try-except for exception handling
try:
	nested_value = my_dict['outer']['inner']
	print("Nested Key 'inner' exists with value:", nested_value)
except KeyError:
	print("Nested Key 'inner' does not exist.")
