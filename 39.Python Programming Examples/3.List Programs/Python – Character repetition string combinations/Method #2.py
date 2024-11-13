# Python3 code to demonstrate working of
# Character repetition string combinations
# Using product() + join() + loop
from itertools import product

# initializing list
test_list = ["gfg", "is", "best"]

# printing original list
print("The original list is : " + str(test_list))

# repeat list
rep_list = [3, 5, 2]

# * operator performs repetitions
# list comprehension encapsulates logic
res = [''.join(sub * ele1 for sub in ele2)
	for ele2, ele1 in product(test_list, rep_list)]

# printing result
print("All repetition combinations strings : " + str(res))
