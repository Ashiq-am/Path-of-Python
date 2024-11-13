# super class
class Base:
	# constructor to initialize attributes
	def __init__(self, name, roll, age):
		self.name = name
		self.roll = roll
		self.age = age

# sub class
class Sub(Base):
	# constructor to initialize attributes of both Base and Sub class
	def __init__(self, name, roll, age):
		super().__init__(name, roll, age)

	# method to display information
	def display(self):
		print(f" Name: {self.name}\n Roll: {self.roll}\n Age: {self.age}")

# creating an object of Sub class
obj = Sub("Sonali", 58, 24)
obj.display()
