#python code to illustrate the lack of
#support for inheritance in type()

class MyDict(dict):
	"""A normal dict, that is always created with an "initial" key"""
	def __init__(self):
		self["initial"] = "some data"

d = MyDict()
print(type(d) == dict)
print(type(d) == MyDict)

d = dict()
print(type(d) == dict)
print(type(d) == MyDict)
