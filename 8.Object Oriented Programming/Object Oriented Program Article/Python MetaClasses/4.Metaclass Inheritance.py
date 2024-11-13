class MetaCls(type):
    """A sample metaclass without any functionality"""

    def __new__(cls, clsname, supercls, attrdict):
        return super(MetaCls, cls).__new__(cls, clsname, supercls, attrdict)


C = MetaCls('C', (object,), {})


## class A inherits from MetaCls
class A(C):
    pass


print(type(A))
