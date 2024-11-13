class MyClass:
	class_variable = "Hello from MyClass"

	@classmethod
	def get_class_variable(cls):
		return cls.class_variable

# Using without creating an object
print(MyClass.get_class_variable())
