class MyString(str):
	def splitfields(self, sep=None):
		if sep is None:
			return self.split()
		else:
			return self.split(sep)

# Splitting a string into fields using whitespace as delimiter
str1 = "The quick brown fox"
fields1 = MyString(str1).splitfields()
print(fields1)


# Splitting a string into fields using a specific delimiter
str2 = "apple,banana,orange"
fields2 = MyString(str2).splitfields(",")
print(fields2)
