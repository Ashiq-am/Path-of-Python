class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

# List of tuples containing person attributes
person_attributes = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Create Person objects using a for loop
people = []
for name, age in person_attributes:
	person = Person(name, age)
	people.append(person)

# Print the details of each person
for person in people:
	print(f"Name: {person.name}, Age: {person.age}")
