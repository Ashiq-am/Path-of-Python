# Creating a class
class Demo:

	# Declaring public method
	def f(self):
		print("Public method")

	# Declaring private method
	def __f(self):
		print("Private method")


# Driver's code
obj = Demo()
obj.f()

print("Using the concept of name mangling")
obj._Demo__f()

print("Without using name mangling")
obj.__f()
