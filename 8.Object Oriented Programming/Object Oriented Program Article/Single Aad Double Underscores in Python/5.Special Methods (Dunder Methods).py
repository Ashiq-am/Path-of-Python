class MySpecialClass:
	def __str__(self):
		return "This is a special class"

# The __str__ method is a special method invoked by the str() function.
obj = MySpecialClass()
print(str(obj))
