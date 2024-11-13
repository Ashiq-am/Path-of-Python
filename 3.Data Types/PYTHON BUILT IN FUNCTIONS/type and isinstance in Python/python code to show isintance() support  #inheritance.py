#python code to show isintance() support
#inheritance
class MyDict(dict):
	"""A normal dict, that is always created with an "initial" key"""
	def __init__(self):
		self["initial"] = "some data"

d = MyDict()
print(isinstance(d, MyDict))
print(isinstance(d, dict))

d = dict()
print(isinstance(d, MyDict))
print(isinstance(d, dict))
