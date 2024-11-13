class MyString(str):
	def splitfields(self, sep=None):
		if sep is None:
			return self.split()
		else:
			return self.split(sep)

class MySet(set):
	def splitfields(self, sep=None):
		str_set = " ".join(self)
		return MyString(str_set).splitfields(sep)

# Splitting a set into fields using whitespace as delimiter
set1 = {"The", "quick", "brown", "fox"}
fields5 = MySet(set1).splitfields()
print(fields5)


# Splitting a set into fields using a specific delimiter
set2 = {"apple", "banana", "orange"}
fields6 = MySet(set2).splitfields(",")
print(fields6)
