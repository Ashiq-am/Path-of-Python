class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


# Creating an instance of the class
person1 = Person("Kishan", 20)

# Calling the instance method
print(person1.introduce())  # Output: Hi, I'm Kishan and I'm 30 years old.