import abc


class AbstractClass(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def abstractName(self):
		pass

class InvalidSubClass(AbstractClass):
	pass

isc = InvalidSubClass()
