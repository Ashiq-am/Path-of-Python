class MyString(str):
	def splitfields(self, sep=None):
		if sep is None:
			return self.split()
		else:
			return self.split(sep)

# Splitting a list into fields using whitespace as delimiter
lst1 = ["The", "quick", "brown", "fox"]
fields3 = MyString(" ".join(lst1)).splitfields()
print(fields3)

# Splitting a list into fields using a specific delimiter
lst2 = ["apple", "banana", "orange"]
fields4 = MyString(",".join(lst2)).splitfields(",")
print(fields4)
