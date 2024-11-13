import inspect


class MyClass:
	def method1(self):
		pass

	def method2(self):
		pass

	def method3(self):
		pass


# Get a list of methods using inspect module
methods_list = [method[0] for method in inspect.getmembers(
	MyClass, predicate=inspect.ismethod)]

print("Methods using inspect module:", methods_list)
