try:
	# Attempting to import a function that does not exist in the module
	from example_module import non_existent_function
except ImportError as e:
	print(f"ImportError: {e}")
