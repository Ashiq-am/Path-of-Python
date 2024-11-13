class GFG:

	def __init__(self, val):
		self.val = val

obj1 = GFG("Geeks")
obj2 = GFG("ForGeeks")
obj3 = obj1 + obj2
print(obj3.val)
