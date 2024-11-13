# Python3 code to demonstrate
# 3 element sum
# using itertools.combination()
from itertools import combinations

# function to get the sum
def test(val):
	return sum(val) == 9

# initializing list
test_list = [4, 1, 3, 2, 6, 5]

# initializing sum
summation = 9

# printing original list
print("The original list : " + str(test_list))

# using itertools.combination()
# 3 element sum
res = list(filter(test, list(combinations(test_list, 3))))

# print result
print("The 3 sum element list is : " + str(res))
