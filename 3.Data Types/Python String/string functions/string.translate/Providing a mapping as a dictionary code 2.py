# Python 3 Program to show working
# of translate() method

# specifying the mapping
# using ASCII
translation = {103: None, 101: None, 101: None}

string = "geeks"
print("Original string:", string)

# translate string
print("Translated string:",
	string.translate(translation))
