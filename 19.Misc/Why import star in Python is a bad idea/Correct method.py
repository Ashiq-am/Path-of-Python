# import the module a as l
import a as l

def sum (x, y):
	return x + y

# calls the self-defined sum function
print (sum (2, 6))

# calls the sum function defined in the module a
print (l.sum(2, 6))
