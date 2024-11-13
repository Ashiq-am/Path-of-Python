# importing the module
from datetime import datetime

# sample function that returns square
# of the value passed
def print_square(x):
	return (x**2)

# records the time at this instant of
# the program in HH:MM:SS format
start = datetime.now()

# calls the function
print_square(3)

# records the time at this instant of the
# program in HH:MM:SS format
end = datetime.now()

# printing the execution time by subtracting
# the time before the function from
# the time after the function
print(end-start)
