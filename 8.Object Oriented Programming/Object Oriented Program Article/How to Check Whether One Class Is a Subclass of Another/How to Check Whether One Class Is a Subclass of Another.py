# Define a base class
class Animal:
    pass

# Define a subclass
class Dog(Animal):
    pass

# Define another subclass
class Labrador(Dog):
    pass

# Check subclass relationships
print(issubclass(Dog, Animal))
print(issubclass(Labrador, Dog))
print(issubclass(Labrador, Animal))
print(issubclass(Animal, Dog))
print(issubclass(Dog, Labrador))

# Check using non-related classes
class Car:
    pass

print(issubclass(Car, Animal))
print(issubclass(Car, object))
