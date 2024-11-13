import abc


class MySequence(metaclass=abc.ABCMeta):
	pass

MySequence.register(list)
MySequence.register(tuple)

a = [1, 2, 3]
b = ('x', 'y', 'z')

print('List instance:', isinstance(a, MySequence))
print('Tuple instance:', isinstance(b, MySequence))
print('Object instance:', isinstance(object(), MySequence))
