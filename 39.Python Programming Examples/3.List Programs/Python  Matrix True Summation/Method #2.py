# Python 3 code to demonstrate
# Matrix True Summation
# using sum()+ map()
from itertools import chain

# initializing list
test_list = [[3, True], [True, 6], [True, 9]]

# printing original list
print ("The original list is : " + str(test_list))

# using sum()+ map()
# Matrix True Summation
res = sum(map(lambda i: i == True, chain.from_iterable(test_list)))

# printing result
print ("The number of True elements: " + str(res))
