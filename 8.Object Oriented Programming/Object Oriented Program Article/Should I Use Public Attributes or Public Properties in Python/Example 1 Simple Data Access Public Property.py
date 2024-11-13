class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


person = Person("Alice")
print(person.name)  # Output: Alice
person.name = "Bob"
print(person.name)  # Output: Bob
