import abc

class AbstractClass(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def abstractName(self):
		pass

class ValidSubClass(AbstractClass):
	def abstractName(self):
		return 'Abstract 1'

vc = ValidSubClass()
print(vc.abstractName())
