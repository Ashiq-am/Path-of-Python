# Python3 code to demonstrate
# Mean of consecutive Sublist
# using itertools.islice() + sum()
import itertools

# initializing list
test_list = [4, 7, 8, 10, 12, 15, 13, 17, 14]

# printing original list
print("The original list : " + str(test_list))

# using itertools.islice() + sum()
# Mean of consecutive Sublist
res = [sum(list(itertools.islice(test_list, i, i + 3))) / 3 for i in range(0, len(test_list), 3)]

# printing result
print("The grouped average list is : " + str(res))
