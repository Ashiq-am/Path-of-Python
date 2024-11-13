# variable number of keyword arguments passed

# function definition
def displayArgument(**arguments):
	for arg in arguments.items():
		print(arg)

# function call
displayArgument(argument1 ="Geeks", argument2 = 4,
				argument3 ="Geeks")
