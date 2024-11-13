class MyClass:
	def method1(self):
		pass

	def method2(self):
		pass

	def method3(self):
		pass


# Get a list of methods using vars()
methods_list = [method for method in vars(MyClass) if callable(
	getattr(MyClass, method)) and not method.startswith("__")]

print("Methods using vars():", methods_list)
