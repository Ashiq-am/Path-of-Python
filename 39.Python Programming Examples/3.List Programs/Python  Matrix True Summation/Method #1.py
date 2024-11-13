# Python 3 code to demonstrate
# Matrix True Summation
# using sum() + generator expression
from itertools import chain

# initializing list
test_list = [[3, False], [False, 6], [False, 9]]

# printing original list
print ("The original list is : " + str(test_list))

# using sum() + generator expression
# Matrix True Summation
res = sum(1 for i in chain.from_iterable(test_list) if i == True)

# printing result
print ("The number of True elements: " + str(res))
