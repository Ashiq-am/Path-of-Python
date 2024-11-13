# defining the class.
class gfg:
    # defining the slots.
    __slots__ = ('course', 'price')

    def __init__(self):
        # initializing the values
        self.course = 'oops'
        self.price = 5999


# create an object of gfg class
a = gfg()

# print the slot
print(a.__slots__)

# print the slot variable
print(a.course, a.price)

# change the value of the variable
a.course = 'System Design'

# print the slot variable
print(a.course, a.price)

# change the value of the variable
a.price = 9999

# print the slot variable
print(a.course, a.price)
