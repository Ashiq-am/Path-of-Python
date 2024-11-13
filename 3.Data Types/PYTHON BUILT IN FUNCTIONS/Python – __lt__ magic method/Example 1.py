class GFG:
	def __lt__(self, other):
		return "YES"
obj1 = GFG()
obj2 = GFG()

print(obj1 < obj2)
print(type(obj1 < obj2))
