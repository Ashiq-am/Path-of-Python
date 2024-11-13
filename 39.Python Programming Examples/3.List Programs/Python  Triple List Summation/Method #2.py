# Python3 code to demonstrate
# Triple List Summation
# using itertools.chain() + sum()
from itertools import chain

# initializing lists
test_list1 = [1, 3, 5, 5, 4]
test_list2 = [4, 6, 2, 8, 10]
test_list3 = [7, 5, 2, 9, 11]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
print("The original list 3 is : " + str(test_list3))

# using itertools.chain() + sum()
# Triple List Summation
test_list1 = sum(list(chain(test_list1, test_list2, test_list3)))

# printing result
print("The summed and modified list is : " + str(test_list1))
