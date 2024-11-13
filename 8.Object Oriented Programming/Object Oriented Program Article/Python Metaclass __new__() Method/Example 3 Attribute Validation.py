class ValidationMeta(type):
    def __new__(cls, name, bases, dct):
        # Ensure 'value' attribute is always an integer
        if 'value' in dct and not isinstance(dct['value'], int):
            raise TypeError("'value' must be an integer.")
        instance = super().__new__(cls, name, bases, dct)
        return instance

class IntegerClass(metaclass=ValidationMeta):
    value = 42

try:
    invalid_obj = IntegerClass(value='not_an_integer')
except TypeError as e:
    print(e)
