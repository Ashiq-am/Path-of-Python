def get_values():
	# Function without a return statement
	return

# Attempting to unpack values from the result
result = get_values()
try:
	a, b = result # Raises "Cannot Unpack Non-iterable NoneType Objects" error
except TypeError as e:
	print(f"Error: {e}")
