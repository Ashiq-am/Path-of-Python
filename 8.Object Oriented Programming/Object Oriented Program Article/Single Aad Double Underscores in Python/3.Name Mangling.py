class MyClass:
	def __init__(self):
		self.__private_variable = 42

obj = MyClass()
# Raises AttributeError; the name is now _MyClass__private_variable
print(obj._MyClass__private_variable)

print(obj.__private_variable)
