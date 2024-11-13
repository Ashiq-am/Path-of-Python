import six


class MetaCls(type):
    def __new__(cls, name, bases, attrs):
        return super(MetaCls, cls).__new__(cls, name, bases, attrs)


class C(six.with_metaclass(MetaCls)):
    pass


print(type(C))
