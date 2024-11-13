class SingletonMeta(type):
    _instances = {}

    def __new__(cls, name, bases, dct):
        if name not in cls._instances:
            cls._instances[name] = super().__new__(cls, name, bases, dct)
        return cls._instances[name]

class SingletonClass(metaclass=SingletonMeta):
    pass

obj1 = SingletonClass()
obj2 = SingletonClass()

print(obj1 is obj2)
