class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self._value = new_value
obj = MyClass("initial value")
print(obj.value)
obj.value = "new value"
print(obj.value)