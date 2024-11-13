# Python3 code to demonstrate
# largest possible number in list
# using itertools.permutation() + join() + max()
from itertools import permutations

# initializing list
test_list = [23, 65, 98, 3, 4]

# printing original list
print ("The original list is : " + str(test_list))

# using itertools.permutation() + join() + max()
# largest possible number in list
res = int(max((''.join(i) for i in permutations(str(i)
					for i in test_list)), key = int))

# printing result
print ("The largest possible number : " + str(res))
