# Python3 code to demonstrate working of
# Disjoint Strings across Lists
# Using set() + yield [ generator ] + reduce() + recursion
from functools import reduce

# helper function
def dis_pairs(dpair, res=[]):

	# checking for disjoint pair
	if not dpair and not reduce(lambda a, b: set(a) & set(b), res):
		yield tuple(res)

	# recurring for subsequent pairs
	elif dpair:
		yield from [idx for k in dpair[0] for idx in dis_pairs(dpair[1:], res + [k])]


# initializing lists
test_list1 = ["haritha", "is", "best"]
test_list2 = ["she", "loves", "papaya"]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# calling function
res = list(dis_pairs([test_list1, test_list2]))

# printing result
print("All possible Disjoint pairs : " + str(res))
