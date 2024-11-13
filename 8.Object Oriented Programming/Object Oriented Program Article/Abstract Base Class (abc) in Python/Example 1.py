import abc


class AbstractClass(metaclass=abc.ABCMeta):
	def abstractfunc(self):
		return None


print(AbstractClass.register(dict))
