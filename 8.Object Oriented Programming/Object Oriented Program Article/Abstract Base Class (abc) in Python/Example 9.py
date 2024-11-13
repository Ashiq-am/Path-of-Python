import abc


class AbstractClass(metaclass=abc.ABCMeta):
	@property
	@abc.abstractmethod
	def abstractName(self):
		pass


class ValidSubClass(AbstractClass):
	@property
	def abstractName(self):
		return 'Abstract 1'


vc = ValidSubClass()
print(vc.abstractName)
