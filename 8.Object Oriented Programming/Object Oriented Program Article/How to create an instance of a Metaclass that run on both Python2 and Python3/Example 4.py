import six


class MetaCls(type):
    def __new__(cls, name, bases, attrs):
        return super(MetaCls, cls).__new__(cls, name, bases, attrs)


@six.add_metaclass(MetaCls)
class C(object):
    pass


print(type(C))
