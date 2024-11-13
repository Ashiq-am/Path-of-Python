class MetaCls(type):
    def __new__(cls, name, bases, attrs):
        return super(MetaCls, cls).__new__(cls, name, bases, attrs)


class C(object):
    __metaclass__ = MetaCls


print(type(C))
