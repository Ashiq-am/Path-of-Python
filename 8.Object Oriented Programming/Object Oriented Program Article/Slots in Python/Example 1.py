# defining the class.
class gfg:
    # defining the slots.
    __slots__ = ('course', 'price')

    def __init__(self):
        # initializing the values
        self.course = 'DSA Self Paced'
        self.price = 3999


# create an object of gfg class
a = gfg()

# print the slot
print(a.__slots__)

# print the slot variable
print(a.course, a.price)
