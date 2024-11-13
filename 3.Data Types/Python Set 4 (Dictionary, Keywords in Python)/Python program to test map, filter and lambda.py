# Python program to test map, filter and lambda

# Function to test map
def cube(x):
	return x**2

# Driver to test above function

# Program for working of map
print("MAP EXAMPLES")
cubes = map(cube, range(10))
print(cubes)

print("LAMBDA EXAMPLES")

# first parentheses contains a lambda form, that is
# a squaring function and second parentheses represents
# calling lambda
print((lambda x: x**2)(5))

# Make function of two arguments that return their product
print((lambda x, y: x*y)(3, 4))


print("FILTER EXAMPLE")
special_cubes = filter(lambda x: x > 9 and x < 60, cubes)
print(special_cubes)
