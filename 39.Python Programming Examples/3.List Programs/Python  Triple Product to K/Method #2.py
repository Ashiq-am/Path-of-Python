# Python3 code to demonstrate
# Triple Product to K
# using itertools.combination()
from itertools import combinations


# function to get the product
def test(val):
    prod = 1
    for ele in val:
        prod *= ele
    return (prod == 24)


# initializing list
test_list = [4, 1, 3, 2, 6, 12]

# initializing product
product = 24

# printing original list
print("The original list : " + str(test_list))

# using itertools.combination()
# 3 element product
res = list(filter(test, list(combinations(test_list, 3))))

# print result
print("The 3 product element list is : " + str(res))
