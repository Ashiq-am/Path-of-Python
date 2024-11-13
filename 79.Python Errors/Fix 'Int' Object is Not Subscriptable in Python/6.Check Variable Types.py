# Checking variable type before using subscript notation
number = 42
if isinstance(number, (str, list)):
	print(number[0])
else:
	print(
		f"Error: Variable type '{type(number).__name__}' is not subscriptable.")
