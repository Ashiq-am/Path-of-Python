# Python3 code to demonstrate working of
# Mutiple Column Sort in Tuples
# Using itemgetter() + sorted()
from operator import itemgetter

# initializing list
test_list = [(6, 7), (6, 5), (1, 4), (8, 10)]

# printing original list
print("The original list is : " + str(test_list))

# Mutiple Column Sort in Tuples
# Using itemgetter() + sorted()
res = sorted(test_list, key = itemgetter(1))
res = sorted(res, key = itemgetter(0), reverse = True)

# printing result
print("The sorted records : " + str(res))
