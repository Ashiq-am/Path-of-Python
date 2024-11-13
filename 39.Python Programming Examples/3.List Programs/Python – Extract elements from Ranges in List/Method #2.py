# Python3 code to demonstrate working of
# Extract elements from Ranges in List
# Using list comprehension
from itertools import chain

# initializing list
test_list = [4, 5, 4, 6, 7, 5, 4, 5, 4, 6, 4, 6, 9, 8]

# printing original list
print("The original list is : " + str(test_list))

# initializing ranges
range_list = [(2, 4), (7, 8), (10, 12)]

# using one-liner to solve this problem
res = list(chain.from_iterable([test_list[ele[0] : ele[1] + 1] for ele in range_list]))

# printing result
print("Ranges elements : " + str(res))
