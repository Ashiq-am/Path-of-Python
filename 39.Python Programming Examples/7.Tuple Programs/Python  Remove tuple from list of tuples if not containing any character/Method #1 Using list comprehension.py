# Python code to remove all those
# elements from list of tuple
# which does not contains any alphabet.

# List initialization
List = [(', ', 12), ('Paras', 5),
		('jain.', 11), ('...', 55),
		('-Geek', 115), ('Geeksfor', 115),
		(':', 63), ('Data', 3), ('-', 15),
		('Structure', 32), ('Algo', 80),]

# Using list comprehension
out = [(a, b) for a, b in List
	if any(c.isalpha() for c in a)]

# Printing output
print(out)
