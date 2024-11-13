import re

def is_float_regex(value):
	return bool(re.match(r'^[-+]?[0-9]*\.?[0-9]+$', value))

input_string = "123.45"
result = is_float_regex(input_string)
print(f"String: {input_string}\nCan be converted to float: {result}")
