class Animal:
	def __init__(self, name):
		self.name = name

	def make_sound(self):
		pass

class Dog(Animal):
	def make_sound(self):
		return "Woof!"

# Creating instances
generic_animal = Animal("Generic Animal")
dog_instance = Dog("Buddy")

# Accessing attributes and methods
print(generic_animal.name) # Output: Generic Animal
print(dog_instance.name) # Output: Buddy
print(dog_instance.make_sound()) # Output: Woof!
