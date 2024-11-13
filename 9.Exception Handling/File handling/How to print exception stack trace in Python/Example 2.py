# import required libraries
import traceback
import sys

# initialising variables
a = 4
b = 0

# exception handling
try:
	value = a / b

except:
	# printing stack trace
	traceback.print_exception(*sys.exc_info())

# out of try-except
# this statement is to show
# that program continues
# normally after an exception is handled
print("end of program")
