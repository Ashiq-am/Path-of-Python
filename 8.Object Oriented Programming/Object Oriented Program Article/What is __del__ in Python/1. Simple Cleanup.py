class SimpleObject:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"SimpleObject '{self.name}' is being destroyed.")


# Creating and deleting an object
obj = SimpleObject('A')
del obj  # Explicitly deleting the object
