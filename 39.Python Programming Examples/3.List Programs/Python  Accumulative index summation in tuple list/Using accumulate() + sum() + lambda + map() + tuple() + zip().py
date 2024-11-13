# Python3 code to demonstrate working of
# Accumulative index summation in tuple list
# Using accumulate() + sum() + lambda + map() + tuple() + zip()
from itertools import accumulate

# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4, 10)]

# printing original list
print("The original list : " + str(test_list))

# Accumulative index summation in tuple list
# Using accumulate() + sum() + lambda + map() + tuple() + zip()
res = list(accumulate(test_list, lambda i, j: tuple(map(sum, zip(i, j)))))

# printing result
print("Accumulative index summation of tuple list : " + str(res))
