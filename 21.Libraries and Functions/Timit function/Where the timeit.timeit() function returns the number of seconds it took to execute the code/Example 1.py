# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = ''' 
def example(): 
	mylist = [] 
	for x in range(100): 
		mylist.append(sqrt(x)) 
'''

# timeit statement
print(timeit.timeit(setup = mysetup,
					stmt = mycode,
					number = 10000))















"""

***The output of above program will be the execution time(in seconds) for 10000 iterations of the code snippet 
passed to timeit.timeit() function.

Note: Pay attention to the fact that the output is the execution time of number times iteration of the code 
snippet, not the single iteration. For a single iteration exec. time, divide the output time by number.

***The program is pretty straight-forward. All we need to do is to pass the code as a string to the timeit.timeit() 
function.


***It is advisable to keep the import statements and other static pieces of code in setup argument.

"""
