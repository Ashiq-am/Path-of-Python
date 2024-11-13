# Python3 code to demonstrate working of
# Test if all strings are mutually disjoint
# Using any() + intersection() + enumerate()

# initializing list
test_list = ["gfg", "is", "bet"]

# printing original list
print("The original list is : " + str(test_list))

# performing intersection of each string with every other
res = not any(set(list(sub1)).intersection(set(list(sub2)))
			for idx, sub1 in enumerate(test_list)
			for sub2 in test_list[idx + 1:])

# printing result
print("Are strings mutually disjoint? : " + str(res))
