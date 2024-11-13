# importing the module
import sys

# function definition
def add(a, b):
	print("Result", a + b)

# fetching the arguments
arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

# displaying the arguments
print(arg1, arg2)

# calling the function
add(arg1, arg2)
