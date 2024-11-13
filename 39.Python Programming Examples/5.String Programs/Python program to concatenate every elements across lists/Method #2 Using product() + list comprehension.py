# Python3 code to demonstrate working of
# All elements concatenation across lists
# Using product() + list comprehension
from itertools import product

# initializing lists
test_list1 = ["gfg", "is", "best"]
test_list2 = ["love", "CS"]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# concatenation using formatting and pairing using product
res = ['%s %s' % (ele[0], ele[1]) for ele in product(test_list1, test_list2)]

# printing result
print("The paired combinations : " + str(res))
