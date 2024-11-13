#Python code to illustrate duck typing

class User(object):
	def __init__(self, firstname):
		self.firstname = firstname

	@property
	def name(self):
		return self.firstname

class Animal(object):
	pass

class Fox(Animal):
	name = "Fox"

class Bear(Animal):
	name = "Bear"

# Use the .name attribute (or property) regardless of the type
for a in [User("Geeksforgeeks"), Fox(), Bear()]:
	print(a.name)












#python code to illustrate the lack of
#support for inheritance in type()

class MyDict(dict):
	"""A normal dict, that is always created with an "initial" key"""
	def __init__(self):
		self["initial"] = "some data"

d = MyDict()
print(type(d) == dict)
print(type(d) == MyDict)

d = dict()
print(type(d) == dict)
print(type(d) == MyDict)












#python code to show isintance() support
#inheritance
class MyDict(dict):
	"""A normal dict, that is always created with an "initial" key"""
	def __init__(self):
		self["initial"] = "some data"

d = MyDict()
print(isinstance(d, MyDict))
print(isinstance(d, dict))

d = dict()
print(isinstance(d, MyDict))
print(isinstance(d, dict))


