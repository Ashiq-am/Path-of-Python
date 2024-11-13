# Python3 code to demonstrate
# cyclic iteration in list using itertools
from itertools import cycle, islice, dropwhile

# initializing tuple list
test_list = [5, 4, 2, 3, 7]

# printing original list
print ("The original list is : " + str(test_list))

# starting index
K = 3

# using itertools methods for
# cyclic iteration in list
cycling = cycle(test_list)
skipping = dropwhile(lambda x: x != K, cycling)
slicing = islice(skipping, None, len(test_list))
slicing = list(slicing)

# printing result
print ("The cycled list is : " + str(slicing))
