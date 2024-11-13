# Python3 code to demonstrate working of
# Repetitive Interleave 2 lists
# Using chain() + zip() + cycle()
from itertools import cycle, chain

# initializing lists
test_list1 = list('abc')
test_list2 = [5, 7, 3, 0, 1, 8, 4]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# zip() combining list, after Repetitiveness using cycle()
# chain() gets interleaved done
res = list(chain(*zip(cycle(test_list1), test_list2)))

# printing result
print("The interleaved list : " + str(res))
