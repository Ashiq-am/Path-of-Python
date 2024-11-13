# Python3 code to demonstrate working of
# Alternate Cycling in list
# using reversed() + islice() + iter() + cycle() + next() + list comprehension
from itertools import islice, cycle

# initialize list
test_list = [5, 6, 8, 9, 10, 21, 3]

# printing original list
print("The original list is : " + str(test_list))

# Alternate Cycling in list
# using reversed() + islice() + iter() + cycle() + next() + list comprehension
res = [next(i) for i in islice(cycle((iter(test_list),
									reversed(test_list))), len(test_list))]

# printing result
print("Alternate Cyclic iteration is : " + str(res))
