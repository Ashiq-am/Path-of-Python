# Python program to demonstrate
# AttributeError


class Geeks():

    def __init__(self):
        self.a = 'GeeksforGeeks'


# Driver's code
obj = Geeks()

print(obj.a)

# Raises an AttributeError as there
# is no attribute b
print(obj.b)
