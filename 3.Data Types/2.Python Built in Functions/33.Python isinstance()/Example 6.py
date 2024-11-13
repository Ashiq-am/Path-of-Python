class geeks:
	course = 'DSA'

	def purchase(obj):
		return obj.course


geeks.purchase = classmethod(geeks.purchase)
str(isinstance(geeks.purchase(), str ))
