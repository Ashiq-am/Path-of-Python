class MetaCls(type):
    def __new__(cls, name, bases, attrs):
        return super(MetaCls, cls).__new__(cls, name, bases, attrs)


class C(object, metaclass=MetaCls):
    pass


print('Type of class C:', type(C))
