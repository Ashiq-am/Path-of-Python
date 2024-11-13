# Python3 code to demonstrate
# Summation in Dual element Records List
# using reduce() + add()
from operator import add
from functools import reduce

# Initializing list
test_list = [(6, 7), (2, 4), (8, 9), (6, 2)]

# printing original lists
print("The original list is : " + str(test_list))

# Summation in Dual element Records List
# using reduce() + add()
res = [reduce(add, sub, 0) for sub in test_list]

# printing result
print ("Summation pairs in tuple list : " + str(res))
