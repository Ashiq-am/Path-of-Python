# Python3 code to demonstrate working of
# Concatenate Maximum Tuples
# Using filter() + max() + itemgetter()
from operator import itemgetter

# initializing list
test_list = [("Gfg is best", 8), ("gfg is good", 7),
			("for", 2), ("for all geeks", 8)]

# printing original list
print("The original list is : " + str(test_list))

# getting maximum
max_ele = max(test_list, key=itemgetter(1))[1]

# joining maximum
# filter checks for maximum values and concats
res = " ".join([ele[0]
				for ele in filter(lambda ele: ele[1] == max_ele, test_list)])

# printing result
print("The maximum concatenated strings : " + str(res))
