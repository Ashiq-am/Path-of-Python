# Python 3 code to demonstrate
# find number of elements > k
# using reduce()
from functools import reduce

# initializing list
test_list = [1, 7, 5, 6, 3, 8]

# initializing k
k = 4

# printing list
print ("The list : " + str(test_list))

# using reduce()
# to get numbers > k
count = reduce(lambda sum, j: sum + (1 if j > k else 0), test_list, 0)

# printing the intersection
print ("The numbers greater than 4 : " + str(count))
