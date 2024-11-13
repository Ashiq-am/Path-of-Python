# Python3 code to demonstrate
# to return true value indices.
# using itertools.compress()
from itertools import compress

# initializing list
test_list = [True, False, True, False, True, True, False]

# printing original list
print ("The original list is : " + str(test_list))

# using itertools.compress()
# to return true indices.
res = list(compress(range(len(test_list)), test_list))

# printing result
print ("The list indices having True values are : " + str(res))
