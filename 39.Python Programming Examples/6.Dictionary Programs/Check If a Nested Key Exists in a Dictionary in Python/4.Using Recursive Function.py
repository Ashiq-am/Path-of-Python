# Recursive function to check nested key existence
def nested_key_exists(d, keys):
	if keys and d:
		return nested_key_exists(d.get(keys[0]), keys[1:])
	return not keys and d is not None

# Example Dictionary
my_dict = {'outer': {'inner': 'value'}}

# Check if 'outer' -> 'inner' exists
if nested_key_exists(my_dict, ['outer', 'inner']):
	print("Nested Key 'inner' exists.")
else:
	print("Nested Key 'inner' does not exist.")
