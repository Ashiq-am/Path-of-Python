# Define the custom object class
class CustomObject:
    def __init__(self, name, score):
        self.name = name
        self.score = score


# Create a tuple of custom objects
custom_tuple = (CustomObject("Alice", 85),
                CustomObject("Bob", 92),
                CustomObject("Charlie", 78))

# Sort the tuple by the 'score' property in descending order
sorted_tuple = sorted(custom_tuple, key=lambda x: x.score, reverse=True)

# Print the sorted tuple
for obj in sorted_tuple:
    print(obj.name, obj.score)
