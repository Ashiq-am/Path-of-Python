# Class definition: Blueprint for creating objects
class Animal:
    # Constructor (__init__): Initializes the object with attributes
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Method: Function inside a class
    def speak(self):
        print(f"{self.name} makes a sound!")


# Inheritance: Dog class inherits from Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Calls the constructor of Animal class
        self.breed = breed

    # Method Overriding: Overriding speak method of the Animal class
    def speak(self):
        print(f"{self.name}, a {self.breed}, barks!")


# Encapsulation: Hiding the internal state (age) of the class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private variable, cannot be accessed directly

    # Getter method to access private attribute __age
    def get_age(self):
        return self.__age

    # Setter method to modify private attribute __age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")


# Polymorphism: Using the same method name for different behavior
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")  # Calls the constructor of Animal class with 'Cat' as species

    def speak(self):
        print(f"{self.name} meows!")


# Abstraction: Hiding complex details in a method
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        # In a real-world scenario, this method could be more complex
        print("Engine started... Vroom!")


# Creating objects
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")  # This will now work without error
person = Person("Alice", 30)
car = Car("Tesla", "Model S")

# Using objects and demonstrating OOPs concepts
print(f"{dog.name} is a {dog.species}")
dog.speak()  # Method Overriding (Polymorphism)

cat.speak()  # Polymorphism: Different behavior, same method name

print(f"{person.name} is {person.get_age()} years old.")
person.set_age(35)
print(f"New age of {person.name}: {person.get_age()}")

car.start_engine()  # Abstraction: Details hidden in the method
