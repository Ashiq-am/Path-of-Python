# Ininitalizing a dictionary
myDict = {1: ("Apple", "Boy", "Cat"),
		2: ("Geeks", "For", "Geeks"),
		3: ("I", "Am", "Learning", "Python")}

# iterate over all tuples using
# values() method
for i in myDict.values():
	for j in i:
		print(j)
	print(" ")
