# Python code to remove all those
# elements from list of tuple
# which does not contains any alphabet.

# List initialization
List = [(', ', 12), ('Paras', 5),
		('jain.', 11), ('...', 55),
		('-Geek', 115), ('Geeksfor', 115),
		(':', 63), ('Data', 3), ('-', 15),
		('Structure', 32), ('Algo', 80),]

# Using filter
out = filter(lambda x:any(c.isalpha()
				for c in x[0]), List)

# Converting in list
out = list(out)

# Printing output
print(out)
