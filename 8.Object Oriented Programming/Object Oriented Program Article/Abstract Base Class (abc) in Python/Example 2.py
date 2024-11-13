import abc


class AbstractClass(metaclass=abc.ABCMeta):
	def abstractfunc(self):
		return None


AbstractClass.register(dict)
print(issubclass(dict, AbstractClass))
