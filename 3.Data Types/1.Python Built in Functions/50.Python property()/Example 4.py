# create a class
class gfg:

    # constructor
    def __init__(self, value):
        self._value = value

    # getting the values
    def getter(self):
        print('Getting value')
        return self._value

    # setting the values
    def setter(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    def deleter(self):
        print('Deleting value')
        del self._value

    # create a properties
    value = property(getter, setter, deleter, )


# create a gfg class object
x = gfg('Happy Coding!')
print(x.value)

x.value = 'Hey Coder!'

# deleting the value
del x.value
