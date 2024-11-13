from collections import namedtuple

# Superclass using namedtuple
Base = namedtuple('Base', ['name', 'roll', 'age'])

# Subclass with additional attribute
class Sub(Base):
	def __new__(cls, name, roll, age, extra):
		obj = super(Sub, cls).__new__(cls, name, roll, age)
		obj.extra = extra
		return obj

# Creating an object of the Subclass with data
obj = Sub("Sonali", 58, 24, "Additional Info")

# Displaying information
print(f" Name: {obj.name}\n Roll: {obj.roll}\n Age: {obj.age}\n Extra: {obj.extra}")
