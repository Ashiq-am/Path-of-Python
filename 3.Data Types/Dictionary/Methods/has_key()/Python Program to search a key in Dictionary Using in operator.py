# Python Program to search a key in Dictionary
# Using in operator

dictionary= {1:"Geeks",2:"For",3:"Geeks"}

print("Dictionary: {}".format(dictionary))

# Return True if Present.
if 1 in dictionary:		 # or "dictionary.keys()"
	print(dictionary[1])
else:
	print("{} is Absent".format(1))


# Return False if not Present.
if 5 in dictionary.keys():
	print(dictionary[5])
else:
	print("{} is Absent".format(5))
