class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(person.name)  # Output: Alice
person.name = "Bob"
print(person.name)  # Output: Bob
