class MetaCls(type):
    """A sample metaclass without any functionality"""

    def __new__(cls, clsname, supercls, attrdict):
        return super(MetaCls, cls).__new__(cls, clsname, supercls, attrdict)


A = MetaCls('A', (object,), {})


class NewMetaCls(type):
    """A sample metaclass without any functionality"""

    def __new__(cls, clsname, supercls, attrdict):
        return super(NewMetaCls, cls).__new__(cls, clsname, supercls, attrdict)


NewA = NewMetaCls('NewA', (object,), {})


class C(A, NewA):
    pass
