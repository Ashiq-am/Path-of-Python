# Python3 code to demonstrate
# common element extraction form N lists
# using reduce() + lambda + set()
from functools import reduce

# initializing list of lists
test_list = [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]

# printing original list
print ("The original list is : " + str(test_list))

# common element extraction form N lists
# using reduce() + lambda + set()
res = list(reduce(lambda i, j: i & j, (set(x) for x in test_list)))

# printing result
print ("The common elements from N lists : " + str(res))
