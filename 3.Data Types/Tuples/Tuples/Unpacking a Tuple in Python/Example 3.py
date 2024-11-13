# Python3 code to study about
# unpacking python tuple using function

# function takes normal arguments
# and multiply them
def result(x, y):
	return x * y
# function with normal variables
print (result(10, 100))

# A tuple is created
z = (10, 100)

# Tuple is passed
# function unpacked them

print (result(*z))
