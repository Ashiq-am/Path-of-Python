"""Let’s look at this example and try to understand the difference between a normal
def defined function and lambda function. This is a program that returns the cube of a given value:

"""



# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
	return y*y*y;

g = lambda x: x*x*x
print(g(7))

print(cube(5))
