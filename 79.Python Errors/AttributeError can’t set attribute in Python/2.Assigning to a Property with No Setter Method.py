class MyClass:
    def __init__(self):
        self._property = 10

    @property
    def property(self):
        return self._property


obj = MyClass()
obj.property = 20
