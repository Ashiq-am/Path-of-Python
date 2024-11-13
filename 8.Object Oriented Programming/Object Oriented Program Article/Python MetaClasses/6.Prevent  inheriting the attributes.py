class MetaCls(type):
    def __new__(cls, name, bases, attrs):
        # If abstract class, then skip the metaclass function
        if attrs.pop('abstract', False):
            print('Abstract Class:', name)
            return super(MetaCls, cls).__new__(cls, name, bases, attrs)

        # metaclass functionality
        if 'foo' in attrs and 'bar' in attrs:
            raise TypeError('Class % s cannot contain both foo and bar \
attributes.' % name)
        if 'foo' not in attrs and 'bar' not in attrs:
            raise TypeError('Class % s must provide either a foo \
attribute or a bar attribute.' % name)
        print('Normal Class:', name)
        return super(MetaCls, cls).__new__(cls, name, bases, attrs)


class AbsCls(metaclass=MetaCls):
    abstract = True


class NormCls(metaclass=MetaCls):
    foo = 42
