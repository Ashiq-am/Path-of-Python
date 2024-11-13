def log_method_call(func):
	def wrapper(self, *args, **kwargs):
		print(f"Calling {func.__name__} with instance {self}...")
		result = func(self, *args, **kwargs)
		print(f"{func.__name__} finished. Result: {result}")
		return result
	return wrapper

class Calculator:
	def __init__(self):
		pass # Constructor code here

	@log_method_call
	def add(self, a, b):
		return a + b

# Usage
calc = Calculator()
result = calc.add(3, 5)
