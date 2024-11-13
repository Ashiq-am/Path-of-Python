# Define the custom object class
class CustomObject:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

# Create a tuple of custom objects
custom_tuple = (CustomObject("Alice", 30, 170),
                CustomObject("Bob", 25, 160),
                CustomObject("Charlie", 35, 175))

# Sort the tuple by the 'age' property first, then by the 'height' property
sorted_tuple = sorted(custom_tuple, key=lambda x: (x.age, x.height))

# Print the sorted tuple
for obj in sorted_tuple:
    print(obj.name, obj.age, obj.height)
