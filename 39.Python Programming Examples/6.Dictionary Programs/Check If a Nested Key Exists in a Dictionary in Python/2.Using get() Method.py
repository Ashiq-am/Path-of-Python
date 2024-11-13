# Example Dictionary
my_dict = {'outer': {'inner': 'value'}}

# Safely access nested key using get()
nested_value = my_dict.get('outer', {}).get('inner')
if nested_value is not None:
	print("Nested Key 'inner' exists with value:", nested_value)
else:
	print("Nested Key 'inner' does not exist.")
