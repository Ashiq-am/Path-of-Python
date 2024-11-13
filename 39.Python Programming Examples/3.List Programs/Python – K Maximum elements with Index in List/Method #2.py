# Python3 code to demonstrate working of
# K Maximum elements with Index in List
# Using enumerate() + itemgetter()
from operator import itemgetter

# initializing list
test_list = [5, 3, 1, 4, 7, 8, 2]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 3

# Using enumerate() + itemgetter()
# Making index values pairs at 1st stage
res = list(sorted(enumerate(test_list), key = itemgetter(1)))[-K:]

# printing result
print("K Maximum with indices : " + str(res))
