class MainClass(type):
    def __new__(cls, name, bases, attrs):
        if 'foo' in attrs and 'bar' in attrs:
            raise TypeError('Class % s cannot contain both foo and bar \
attributes.' % name)
        if 'foo' not in attrs and 'bar' not in attrs:
            raise TypeError('Class % s must provide either a foo \
attribute or a bar attribute.' % name)
        else:
            print('Success')

        return super(MainClass, cls).__new__(cls, name, bases, attrs)


class SubClass(metaclass=MainClass):
    foo = 42
    bar = 34


subCls = SubClass()
