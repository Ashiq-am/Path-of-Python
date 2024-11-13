class Person:
	# Class attribute
	species = "Homo sapiens"

	def __init__(self, name, age):
		# Instance attributes
		self.name = name
		self.age = age

	def introduce(self):
		print(f"Hi, I'm {self.name}, {self.age} years old.")

# Creating instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing class attribute
print(f"All humans belong to the species: {Person.species}")

# Accessing instance attributes
person1.introduce()
person2.introduce()
