class MyClass:
    def __init__(self):
        self._property = 10

    @property
    def property(self):
        return self._property

    @property.setter
    def property(self, value):
        self._property = value


obj = MyClass()
obj.property = 20
print(obj.property)  # Output: 20
