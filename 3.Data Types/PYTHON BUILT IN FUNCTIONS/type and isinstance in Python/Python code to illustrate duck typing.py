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
