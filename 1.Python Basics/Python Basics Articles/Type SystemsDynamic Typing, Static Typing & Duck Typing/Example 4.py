class Duck:
	def quack(self):
		print("Quack")

class Goose:
	def quack(self):
		print("Quack Quack")

class Dog:
	def bark(self):
		print("I just bark")

class ItQuacks:
	def __init__(self, animal):
		animal.quack()

ItQuacks(Duck())
ItQuacks(Goose())
ItQuacks(Dog())
