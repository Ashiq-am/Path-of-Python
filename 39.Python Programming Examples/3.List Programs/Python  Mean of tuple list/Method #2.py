# Python3 code to demonstrate working of
# Mean of tuple list
# Using chain() + sum()
from itertools import chain

# Initializing list
test_list = [(1, 4, 5), (7, 8), (2, 4, 10)]

# printing original list
print("The original list is : " + str(test_list))

# Average of tuple list
# Using chain() + sum()
temp = list(chain(*test_list))
res = sum(temp)/ len(test_list)

# printing result
print("The mean of tuple list is : " + str(res))
