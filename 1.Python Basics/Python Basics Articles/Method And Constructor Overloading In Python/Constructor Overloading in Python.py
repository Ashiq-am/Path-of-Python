class Person:
	def __init__(self, name, age=None):
		self.name = name
		self.age = age


# Example Usage
person1 = Person("Alice")
person2 = Person("Bob", 25)

# Output
print(person1.name, person1.age)
print(person2.name, person2.age)
