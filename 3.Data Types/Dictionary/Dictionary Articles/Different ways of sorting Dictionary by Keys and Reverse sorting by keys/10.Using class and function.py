class SortedDisplayDict(dict):
	def __str__(self):
		return "{" + ", ".join("%r: %r" % (key, self[key]) for key in sorted(self)) + "}"


# Initialising dictionary and calling class
my_dict = SortedDisplayDict({"b": 2, "c": 3, "a": 1,"d":4})

# Printing dictionary
print(my_dict)
