def example_function():
	result = None # Initialize the variable before the try block
	try:
		result = some_operation()
	except Exception as e:
		print("An error occurred:", e)
	print(result)
