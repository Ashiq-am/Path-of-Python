class MissingReturnContextManager:
	def __init__(self):
		pass

	def __enter_(self):
		print("Entering the context")
		# Missing return statement

	def __exit__(self, exc_type, exc_value, traceback):
		print("Exiting the context")

# Using the context manager
with MissingReturnContextManager() as cm:
	print("Inside the context")
