class MyClass:
	@classmethod
	def class_method(cls):
		return "Hello from class method"

def class_function():
	return MyClass.class_method()

# Using without creating an object
print(class_function())
