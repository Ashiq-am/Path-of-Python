# Ininitalizing a dictionary
myDict = {1: ("Apple", "Boy", "Cat"),
		2: ("Geeks", "For", "Geeks"),
		3: ("I", "Am", "Learning", "Python")}

print("Tuple mapped with the key 1 =>"),

# Directly printing entire tuple mapped
# with the key 1
print(myDict[1])

print("Tuple mapped with the key 2 =>"),

# Printing tuple elements mapped with
# the key 2 one by one
for each in myDict[2]:
	print(each),

print("")
print("Tuple mapped with the key 3 =>"),

# Accessing tuple elements mapped with
# the key 3 using index
for i in range(0, len(myDict[3])):
	print(myDict[3][i]),
