class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent class initialized with name: {self.name}")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(
            f"Child class initialized with name: {self.name} and age: {self.age}")


# Creating an instance of Child
child_instance = Child("John", 10)
