# program to compute the time of
# execution of any python code using timit

# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time
# is to be measured
mycode = '''
def example():
	mylist = []
	for x in range(100):
		mylist.append(sqrt(x))
'''

# timeit statement
print ("The time of execution of above program is :",
	timeit.timeit(setup = mysetup,
					stmt = mycode,
					number = 10000))
