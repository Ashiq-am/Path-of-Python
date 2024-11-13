class MyDescriptor:
    def __get__(self, instance, owner):
        return "value"
# Incorrect instantiation leading to the TypeError
desc = MyDescriptor()
