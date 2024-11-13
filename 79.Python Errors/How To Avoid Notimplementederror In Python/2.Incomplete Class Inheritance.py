from abc import ABC, abstractmethod

class Animal(ABC):
	@abstractmethod
	def speak(self):
		pass

class Dog(Animal):
	def speak(self):
		raise NotImplementedError("speak() method not implemented for Dog")

# Attempting to instantiate Dog and call speak()
try:
	dog = Dog()
	dog.speak()
except NotImplementedError as e:
	print("NotImplementedError:", e)
