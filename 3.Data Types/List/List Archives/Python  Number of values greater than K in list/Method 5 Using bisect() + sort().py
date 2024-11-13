# Python 3 code to demonstrate
# find number of elements > k
# using bisect() + sort()
from bisect import bisect

# initializing list
test_list = [1, 7, 5, 6, 3, 8]

# initializing k
k = 4

# printing list
print ("The list : " + str(test_list))

# using bisect() + sort()
# to get numbers > k
test_list.sort()
count = len(test_list) - bisect(test_list, k)

# printing the intersection
print ("The numbers greater than 4 : " + str(count))
