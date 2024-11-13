# Python3 code to demonstrate
# Maximum element in consecutive subsets
# using itertools.islice() + max()
import itertools

# initializing list
test_list = [4, 7, 8, 10, 12, 15, 13, 17, 14]

# printing original list
print("The original list : " + str(test_list))

# using itertools.islice() + max()
# Maximum element in consecutive subsets
res = [max(list(itertools.islice(test_list, i, i + 3)))
				for i in range(0, len(test_list), 3)]

# printing result
print("The grouped maximized list is : " + str(res))
