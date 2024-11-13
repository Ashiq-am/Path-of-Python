# Python3 code to demonstrate working of
# Incremental Records Product
# Using accumulate() + loop + lambda + map() + tuple() + zip()
from itertools import accumulate


def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res


# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4, 10)]

# printing original list
print("The original list : " + str(test_list))

# Incremental Records Product
# Using accumulate() + loop + lambda + map() + tuple() + zip()
res = list(accumulate(test_list, lambda i, j: tuple(map(prod, zip(i, j)))))

# printing result
print("Accumulative index product of tuple list : " + str(res))
