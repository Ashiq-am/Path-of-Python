class geeks:
	course = 'DSA'

	def purchase(obj):
		print("Puchase course : ", obj.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()
