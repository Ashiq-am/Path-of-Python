# Python code to demonstrate
# working of getattr()

# declaring class
class GfG:
	name = "GeeksforGeeks"
	age = 24

# initializing object
obj = GfG()

# use of getattr without default
print("Motto is " + getattr(obj, 'motto'))
