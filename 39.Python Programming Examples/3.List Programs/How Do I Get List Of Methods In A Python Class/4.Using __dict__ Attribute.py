class MyClass:
	def method1(self):
		pass

	def method2(self):
		pass

	def method3(self):
		pass


# Get a list of methods using __dict__ attribute
methods_list = [method for method in MyClass.__dict__ if callable(
	getattr(MyClass, method)) and not method.startswith("__")]

print("Methods using __dict__ attribute:", methods_list)
