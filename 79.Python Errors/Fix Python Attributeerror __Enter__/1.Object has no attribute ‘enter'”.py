class MyContextManager:
	def __init__(self):
		pass

	def __enter_(self):
		print("Entering the context")

	def __exit__(self, exc_type, exc_value, traceback):
		print("Exiting the context")

# Using the context manager
with MyContextManager() as cm:
	print("Inside the context")
