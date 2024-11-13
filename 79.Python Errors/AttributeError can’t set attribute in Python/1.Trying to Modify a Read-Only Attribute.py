class MyClass:
    def __init__(self):
        self._readonly_attr = 42

    @property
    def readonly_attr(self):
        return self._readonly_attr


obj = MyClass()
obj.readonly_attr = 100  # Attempting to modify a read-only attribute
