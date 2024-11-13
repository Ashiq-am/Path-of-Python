try:
	# Attempting to import a non-existent module
	import non_existent_module
except ModuleNotFoundError as e:
	print(f"ModuleNotFoundError: {e}")
