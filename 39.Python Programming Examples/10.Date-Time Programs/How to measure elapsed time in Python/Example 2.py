# importing the module
import timeit

# sample function that returns square
# of the value passed
def print_square(x):
	return (x**2)

# using the timeit method and lambda
# expression to get the execution time of
# the function, number defines how many
# times we execute this function
t = timeit.timeit(lambda: print_square(3), number=10)

# printing the execution time
print(t)
