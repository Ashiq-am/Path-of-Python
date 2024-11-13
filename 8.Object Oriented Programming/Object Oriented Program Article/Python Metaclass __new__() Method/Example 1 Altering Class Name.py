class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        # Adding 'Custom' prefix to class name
        name = 'Custom' + name
        instance = super().__new__(cls, name, bases, dct)
        return instance

class MyClass(metaclass=CustomMeta):
    pass

print(MyClass.__name__)
