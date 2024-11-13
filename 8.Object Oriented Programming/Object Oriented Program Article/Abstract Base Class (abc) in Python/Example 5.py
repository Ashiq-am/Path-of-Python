import abc


class MySequence(metaclass=abc.ABCMeta):
	pass

@MySequence.register
class CustomListLikeObjCls(object):
	pass

print(issubclass(CustomListLikeObjCls, MySequence))
