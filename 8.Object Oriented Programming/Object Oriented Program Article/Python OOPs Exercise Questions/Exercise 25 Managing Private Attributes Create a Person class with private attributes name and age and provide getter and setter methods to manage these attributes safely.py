class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self.__name = value
        else:
            print("Invalid name")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self.__age = value
        else:
            print("Invalid age")

# Example usage:
person = Person("John Doe", 30)
print("Name:", person.name)
print("Age:", person.age)
person.name = ""
person.age = -5
