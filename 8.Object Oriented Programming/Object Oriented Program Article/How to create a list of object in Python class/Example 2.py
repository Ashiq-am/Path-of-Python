# Python3 code here for creating class
class geeks:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Sum(self):
        print(self.x + self.y)


# creating list
list = []

# appending instances to list
list.append(geeks(2, 3))
list.append(geeks(12, 13))
list.append(geeks(22, 33))

for obj in list:
    # calling method
    obj.Sum()

# We can also access instances method
# as list[0].Sum() , list[1].Sum() and so on.
