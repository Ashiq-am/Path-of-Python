class Parent:
    def __init__(self, name):
        self.name = name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent's constructor first
        self.age = age


parent = Parent("Alice")
child = Child("Bob", 12)

print("Parent:", parent.name)
print("Child:", child.name, child.age)
