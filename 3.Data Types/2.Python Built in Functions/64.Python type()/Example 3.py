# New class(has no base) class with the
# dynamic class initialization of type()
new = type('New', (object, ),
		dict(var1='GeeksforGeeks', b=2009))

# Print type() which returns class 'type'
print(type(new))
print(vars(new))


# Base class, incorporated
# in our new class
class test:
	a = "Geeksforgeeks"
	b = 2009


# Dynamically initialize Newer class
# It will derive from the base class test
newer = type('Newer', (test, ),
			dict(a='Geeks', b=2018))

print(type(newer))
print(vars(newer))
