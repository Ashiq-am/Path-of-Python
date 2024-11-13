import abc


class AbstractClass(metaclass=abc.ABCMeta):
	@classmethod
	def __subclasshook__(cls, other):
		print('subclass hook:', other)
		hookmethod = getattr(other, 'hookmethod', None)
		return callable(hookmethod)

class SubClass(object):
	def hookmethod(self):
		pass

class NormalClass(object):
	hookmethod = 'hook'


print(issubclass(SubClass, AbstractClass))
print(issubclass(NormalClass, AbstractClass))
