print(repr({"a": 1, "b": 2}))
print(repr([1, 2, 3]))

# Custom class
class C():
	def __repr__(self):
		return "This is class C"

# Converting custom object to
# string
print(repr(C()))
