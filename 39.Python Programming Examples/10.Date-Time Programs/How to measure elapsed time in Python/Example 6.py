# importing the module
import time

# sample function that returns square
# of the value passed
def print_square(x):
	return (x**2)

# records the time in nanoseceonds at
# this instant of the program
start = time.time_ns()

# calls the function
print_square(3)

# records the time in nanoseceonds at this
# instant of the program
end = time.time_ns()

# printing the execution time by subtracting
# the time before the function from
# the time after the function
print(end-start)
