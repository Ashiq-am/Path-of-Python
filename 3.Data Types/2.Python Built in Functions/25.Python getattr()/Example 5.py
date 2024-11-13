# Python code to demonstrate
# working of getattr()

# declaring class
class GfG:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self, x):
        print(f"{self.name} called with parameters '{x}'")
        return


# initializing object
obj = GfG("Vivek", 10)
print(obj)
print(GfG)
print(getattr(obj, 'call'))

getattr(obj, 'call')('arg')
