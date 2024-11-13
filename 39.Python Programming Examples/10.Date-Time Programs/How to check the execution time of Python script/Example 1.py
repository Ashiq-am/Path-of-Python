# program to compute the time
# of execution of any python code
import time

# we initialize the variable start
# to store the starting time of
# execution of program
start = time.time()

# we can take any program but for
# example we have taken the below
# program
a = 0
for i in range(1000):
	a += (i**100)

# now we have initialized the variable
# end to store the ending time after
# execution of program
end = time.time()

# difference of start and end variables
# gives the time of execution of the
# program in between
print("The time of execution of above program is :", end-start)
