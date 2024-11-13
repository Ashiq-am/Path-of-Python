# Superclass
class Base:
	def __init__(self, name, roll, age):
		self.name = name
		self.roll = roll
		self.age = age

# Create a subclass using type.__new__
Sub = type("Sub", (Base,), {})

# Creating an object of the Subclass with data
obj = Sub("Sonali", 58, 24)

# Displaying information
print(f" Name: {obj.name}\n Roll: {obj.roll}\n Age: {obj.age}")
