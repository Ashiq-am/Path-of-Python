class unaryOp(object):
    def __init__(self, value):
        self._value = value

    def __pos__(self):
        print('__pos__ magic method')
        return (+self._value)


up = unaryOp(5)
print(+up)
