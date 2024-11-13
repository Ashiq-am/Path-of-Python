class MetaCls(type):
	"""A sample metaclass without any functionality"""
	def __new__(cls, clsname, superclasses, attributedict):
		print("clsname:", clsname)
		print("superclasses:", superclasses)
		print("attrdict:", attributedict)
		return super(MetaCls, cls).__new__(cls, \
					clsname, superclasses, attributedict)

C = MetaCls('C', (object, ), {})
print("class type:", type(C))
