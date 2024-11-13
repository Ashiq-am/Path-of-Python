class MyMeta(type):
	def __new__(cls, name, bases, dct):
		# Add custom behavior here
		return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
	class_variable = "Hello from MyClass"

# Using without creating an object
print(MyClass.class_variable)
