class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person('Gia', 18), Person('Gio', 22)]
names = [person.name for person in people]
print(names)