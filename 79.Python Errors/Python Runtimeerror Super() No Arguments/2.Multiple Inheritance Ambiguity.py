class Works(type):
	def __new__(cls, *args, **kwargs):
		print([cls,args]) # outputs [<class '__main__.Works'>, ()]
		return super().__new__(cls, args)

class DoesNotWork(type):
	def __new__(*args, **kwargs):
		print([args[0],args[:0]]) # outputs [<class '__main__.doesNotWork'>, ()]
		return super().__new__(args[0], args[:0])

DoesNotWork()
