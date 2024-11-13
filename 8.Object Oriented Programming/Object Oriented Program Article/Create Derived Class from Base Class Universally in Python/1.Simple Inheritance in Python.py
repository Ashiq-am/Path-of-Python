class Animal:
	def __init__(self, species):
		self.species = species

	def make_sound(self):
		pass

class Dog(Animal):
	def __init__(self, breed):
		super().__init__("Dog")
		self.breed = breed

	def make_sound(self):
		return "Woof!"

# Creating an instance of the derived class
my_dog = Dog("Labrador")

# Accessing attributes and methods from both base and derived classes
print(f"Species: {my_dog.species}, Breed: {my_dog.breed}, Sound: {my_dog.make_sound()}")
