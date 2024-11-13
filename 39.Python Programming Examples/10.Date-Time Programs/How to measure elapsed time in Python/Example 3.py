# importing the module
import timeit


# sample function that returns square
# of the value passed
def print_square(x):
	return (x**2)

# using the repeat method and lambda
# expression to get the execution time of
# the function, number defines how many
# times we execute this function and the
# repeat defines the number of times the
# time calculation needs to be done.
t = timeit.repeat(lambda: print_square(3), number=10, repeat=5)

# printing the execution time
print(t)
