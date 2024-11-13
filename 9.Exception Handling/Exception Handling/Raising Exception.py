#The raise statement allows the programmer to force a specific exception to occur.
# The sole argument in raise indicates the exception to be raised.
# This must be either an exception instance or an exception class (a class that derives from Exception).




# Program to depict Raising Exception

try:
	raise NameError("Hi there") # Raise Error
except NameError:
	print("An exception")
	raise # To determine whether the exception was raised or not




#The output of the above code will simply line printed as “An exception” but a Runtime error will also occur in the last due to raise statement in the last line.
# So, the output on your command line will look like





