import abc


class MySequence(metaclass=abc.ABCMeta):
	pass

class CustomListLikeObjCls(object):
	pass

MySequence.register(CustomListLikeObjCls)
print(issubclass(CustomListLikeObjCls, MySequence))
