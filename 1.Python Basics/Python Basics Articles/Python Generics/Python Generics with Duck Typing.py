from typing import TypeVar, Iterable

# Declare type variable
T = TypeVar('T')

def process_data(data: Iterable[T]) -> None:
    for item in data:
        # Check if the object has a quack method, then call it
        if hasattr(item, 'quack') and callable(item.quack):
            item.quack()
        else:
            print(f"This object of type {type(item).__name__} doesn't quack like a duck!")

# Example class
class Duck:
    def quack(self):
        print("Quack!")

# Another class with similar behavior
class AnotherBird:
    def quack(self):
        print("Quack!")

# Using duck typing with process_data function
duck_obj = Duck()
another_bird_obj = AnotherBird()

# Both objects "quack" like a duck
duck_list = [duck_obj, another_bird_obj]

# We can pass duck_list to process_data because both objects have a quack method
process_data(duck_list)
