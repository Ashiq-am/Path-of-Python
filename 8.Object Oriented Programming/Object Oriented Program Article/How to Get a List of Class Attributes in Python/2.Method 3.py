class Number:
    # Class Attributes
    one = 'first'
    two = 'second'
    three = 'third'

    def __init__(self, attr):
        self.attr = attr

    def show(self):
        print(self.one, self.two, self.three, self.attr)


# Driver's code
n = Number(2)
n.show()

# using __dict__ to access attributes
# of the object n along with their values
print(n.__dict__)

# to only access attributes
print(n.__dict__.keys())

# to only access values
print(n.__dict__.values())
