class Grandparent:
    def __init__(self, name):
        self.name = name


class Parent(Grandparent):
    def __init__(self, name, age):
        super().__init__(name)  # Call grandparent's constructor
        self.age = age


class Child(Parent):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)  # Call parent's constructor
        self.hobby = hobby


child = Child("Charlie", 8, "reading")

print("Child:", child.name, child.age, child.hobby)
