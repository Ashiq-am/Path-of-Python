''''''


'''Let’s see another practical example in which we will compare two searching techniques, namely, Binary 
search and Linear search.

Also, here I demonstrate two more features, timeit.repeat function and calling the functions already defined 
in our program.'''









# importing the required modules
import timeit


# binary search function
def binary_search(mylist, find):
    while len(mylist) > 0:
        mid = (len(mylist)) // 2
        if mylist[mid] == find:
            return True
        elif mylist[mid] < find:
            mylist = mylist[:mid]
        else:
            mylist = mylist[mid + 1:]
    return False


# linear search function
def linear_search(mylist, find):
    for x in mylist:
        if x == find:
            return True
    return False


# compute binary search time
def binary_time():
    SETUP_CODE = ''' 
from __main__ import binary_search 
from random import randint'''

    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
binary_search(mylist, find)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # priniting minimum exec. time
    print('Binary search time: {}'.format(min(times)))


# compute linear search time
def linear_time():
    SETUP_CODE = ''' 
from __main__ import linear_search 
from random import randint'''

    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
linear_search(mylist, find) 
	'''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # priniting minimum exec. time
    print('Linear search time: {}'.format(min(times)))


if __name__ == "__main__":
    linear_time()
    binary_time()












"""

***timeit.repeat() function accepts one extra argument, repeat. The output will be a list of the execution 
    times of all code runs repeated a specified no. of times.


***In setup argument, we passed:

                               from __main__ import binary_search
                               from random import randint


This will import the definition of function binary_search, already defined in the program and random library 
function randint.

***As expected, we notice that execution time of binary search is significantly lower than linear search!

"""
