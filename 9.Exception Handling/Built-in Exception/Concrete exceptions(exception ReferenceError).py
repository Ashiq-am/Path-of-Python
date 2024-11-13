import gc
import weakref


class Foo(object):

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('(Deleting %s)' % self)


obj = Foo('obj')
p = weakref.proxy(obj)

print('BEFORE:', p.name)
obj = None
print('AFTER:', p.name)
