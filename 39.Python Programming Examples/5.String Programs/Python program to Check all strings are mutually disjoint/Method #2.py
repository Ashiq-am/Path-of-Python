# Python3 code to demonstrate working of
# Test if all strings are mutually disjoint
# Using

# initializing list
test_list = ["gfg", "is", "bet"]

# printing original list
print("The original list is : " + str(test_list))

# performing concatenation and checking
# for lengths
concats = ''.join(test_list)
res = len(concats) == len(set(concats))

# printing result
print("Are strings mutually disjoint? : " + str(res))
