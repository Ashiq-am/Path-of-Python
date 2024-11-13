# Python3 code to demonstrate
# Subgrouping of i'th index size in list
# using islice() + dictionary comprehension
from itertools import islice

# initializing list
test_list = [4, 7, 8, 10, 12, 15, 13, 17, 14, 5]

# printing original list
print("The original list : " + str(test_list))

# using islice() + dictionary comprehension
# Subgrouping of i'th index size in list
temp = iter(test_list)
res = {key: val for key, val in ((i, list(islice(temp, i)))
				for i in range(1, len(test_list))) if val}

# printing result
print("The grouped dictionary is : " + str(res))
