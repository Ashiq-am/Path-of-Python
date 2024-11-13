# Python program to illustrate the
# formatting of a string using a dictionary

# Initializing a value
value = {"Company": "GeeksforGeeks",
		"Department": "Computer Science"}

# Calling the .format() function
# over the above given value
print("{Company} is a {Department} Portal.".format(**value))
