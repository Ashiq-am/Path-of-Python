class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Example usage:
dog = Dog()
cat = Cat()
dog.speak()
cat.speak()
