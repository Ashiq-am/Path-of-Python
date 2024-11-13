class MyMeta(type):
    def __new__(cls, name, bases, class_dict, arg1, arg2):
        # Access the arguments passed from the class
        print(f"Metaclass received arguments: arg1={arg1}, arg2={arg2}")

        # Call the parent metaclass's __new__ method
        return super().__new__(cls, name, bases, class_dict)


class MyClass(metaclass=MyMeta, arg1="value1", arg2="value2"):
    # Class definition goes here
    pass
