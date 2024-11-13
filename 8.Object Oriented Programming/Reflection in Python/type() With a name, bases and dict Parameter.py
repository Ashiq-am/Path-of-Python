# Python code for type() with a name,
# bases and dict parameter

o1 = type('X', (object,), dict(a='Foo', b=12))

print(type(o1))
print(vars(o1))


class test:
    a = 'Foo'


b = 12

o2 = type('Y', (test,), dict(a='Foo', b=12))
print(type(o2))
print(vars(o2))










#If you need to check type of an object, it is recommended to use Python
# isinstance() function instead.
# It’s because isinstance() function also checks if the given object is an
# instance of the subclass.