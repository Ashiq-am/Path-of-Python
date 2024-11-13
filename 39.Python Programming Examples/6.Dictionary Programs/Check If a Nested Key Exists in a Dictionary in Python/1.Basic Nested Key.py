# Example Dictionary
my_dict = {'outer': {'inner': 'value'}}

# Check if 'inner' key exists inside 'outer'
if 'outer' in my_dict and 'inner' in my_dict['outer']:
	nested_value = my_dict['outer']['inner']
	print("Nested Key 'inner' exists with value:", nested_value)
else:
	print("Nested Key 'inner' does not exist.")
