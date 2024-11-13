class Animal:
	def __init__(self, species):
		self.species = species


class Dog(Animal):
	def __init__(self, name, age):
		super().__init__("Dog")
		self.name = name
		self.age = age


# Creating an instance of the Dog class
dog_instance = Dog("Buddy", 3)

# Accessing attributes from the base class
print(f"{dog_instance.name} is a {dog_instance.species} of age {dog_instance.age} years")
