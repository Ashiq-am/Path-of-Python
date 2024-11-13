class demoClass:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def add(a, b):
		return a + b

	def diff(self):
		return self.a-self.b


# convert the add to a static method
demoClass.add = staticmethod(demoClass.add)

# we can access the method without creating
# the instance of class
print(demoClass.add(1, 2))

# if we want to use properties of a class
# then we need to create a object
Object = demoClass(1, 2)
print(Object.diff())
