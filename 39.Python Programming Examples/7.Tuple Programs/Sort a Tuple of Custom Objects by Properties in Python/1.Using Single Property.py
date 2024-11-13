# Define the custom object class
class CustomObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create a tuple of custom objects
custom_tuple = (CustomObject("Alice", 30),
                CustomObject("Bob", 25),
                CustomObject("Charlie", 35))

# Sort the tuple by the 'age' property
sorted_tuple = sorted(custom_tuple, key=lambda x: x.age)

# Print the sorted tuple
for obj in sorted_tuple:
    print(obj.name, obj.age)
