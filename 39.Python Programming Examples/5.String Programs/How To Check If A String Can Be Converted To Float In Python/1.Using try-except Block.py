def is_float_try_except(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

input_string = "123.45"
result = is_float_try_except(input_string)
print(f"String: {input_string}\nCan be converted to float: {result}")
