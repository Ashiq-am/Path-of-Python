# Python3 code to demonstrate
# Consecutive Subsets Minimum
# using itertools.islice() + min()
import itertools

# initializing list
test_list = [4, 7, 8, 10, 12, 15, 13, 17, 14]

# printing original list
print("The original list : " + str(test_list))

# using itertools.islice() + min()
# Consecutive Subsets Minimum
res = [min(list(itertools.islice(test_list, i, i + 3))) for i in range(0, len(test_list), 3)]

# printing result
print("The grouped minimum list is : " + str(res))
