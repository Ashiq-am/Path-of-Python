class Color:
	def __init__(self, suffix):
		self.suffix = suffix
		self.title = f"Golden {suffix}"

	def __repr__(self):
		return f"Color('{self.suffix}')"


c1 = Color("Yellow")
# create another object with same params as c1
# using eval() on repr()
c2 = eval(repr(c1))

print("c1.title:", c1.title)
print("c2.title:", c2.title)
