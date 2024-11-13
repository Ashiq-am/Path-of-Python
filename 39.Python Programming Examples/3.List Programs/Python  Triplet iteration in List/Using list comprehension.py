# Python3 code to demonstrate
# Triplet iteration in List
# using list comprehension
from itertools import compress

# initializing list
test_list = [0, 1, 2, 3, 4, 5]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension
# Triplet iteration in List
res = [((i), (i + 1) % len(test_list), (i + 2) % len(test_list))
								for i in range(len(test_list))]

# printing result
print ("The triplet list is : " + str(res))
