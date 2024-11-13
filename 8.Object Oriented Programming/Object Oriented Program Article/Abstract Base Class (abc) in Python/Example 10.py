from collections.abc import Sized


class SingleMethod(object):
	def __len__(self):
		return 10


print(issubclass(SingleMethod, Sized))
