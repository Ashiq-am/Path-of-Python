# Python3 code to demonstrate
# Smallest number from list
# using itertools.permutation() + join() + min()
from itertools import permutations

# initializing list
test_list = [23, 65, 98, 3, 4]

# printing original list
print ("The original list is : " + str(test_list))

# using itertools.permutation() + join() + min()
# Smallest number from list
res = int(min((''.join(i) for i in permutations(str(i)
					for i in test_list)), key = int))

# printing result
print ("The smallest possible number : " + str(res))
