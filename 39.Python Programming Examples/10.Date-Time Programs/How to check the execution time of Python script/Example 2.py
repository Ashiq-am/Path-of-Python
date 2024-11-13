# program to compute the time
# of execution of any python code
# for different number of computations
import time

# we initialize a for loop and in each
# iterations store the time of start
# and end of the iterations
for j in range(100, 1100, 100):
	start = time.time()

	# program to iterate the range of
	# below loop increasing the value
	# in each iterations
	a = 0
	for i in range(j):
		a += (i**100)

	# the end variable to store the
	# ending time after execution of
	# program after each iterations
	end = time.time()

	# difference of start and end variables
	# gives the time of execution of the program
	# in between in each iterations
	print("Time for execution of program for {} order of computations: {}".format(
		j, round(end-start, 10)))
