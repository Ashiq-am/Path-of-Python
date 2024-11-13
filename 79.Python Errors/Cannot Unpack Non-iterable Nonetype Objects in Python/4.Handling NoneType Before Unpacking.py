def get_values():
	# Function without a return statement
	return

# Handling NoneType before unpacking
result = get_values()
if result is not None:
	a, b = result
else:
	print("Error: Unable to unpack, result is None")
