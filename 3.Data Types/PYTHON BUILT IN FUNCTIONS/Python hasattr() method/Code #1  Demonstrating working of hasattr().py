# Python code to demonstrate
# working of hasattr()

# declaring class
class GfG :
	name = "GeeksforGeeks"
	age = 24

# initializing object
obj = GfG()

# using hasattr() to check name
print ("Does name exist ? " + str(hasattr(obj, 'name')))

# using hasattr() to check motto
print ("Does motto exist ? " + str(hasattr(obj, 'motto')))
