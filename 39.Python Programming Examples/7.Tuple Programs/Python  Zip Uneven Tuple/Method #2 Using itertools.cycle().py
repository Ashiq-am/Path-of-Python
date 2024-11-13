# Python3 code to demonstrate
# Zip Uneven Tuple
# using itertools.cycle()
from itertools import cycle

# initializing tuples
test_tup1 = (7, 8, 4, 5, 9, 10)
test_tup2 = (1, 5, 6)

# printing original tuples
print ("The original tuple 1 is : " + str(test_tup1))
print ("The original tuple 2 is : " + str(test_tup2))

# using itertools.cycle()
# Zip Uneven Tuple
res = list(zip(test_tup1, cycle(test_tup2)) if len(test_tup1) > len(test_tup2) else zip(cycle(test_tup1), test_tup2))

# printing result
print ("The zipped tuple is : " + str(res))
