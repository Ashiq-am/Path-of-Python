# Python3 code to demonstrate working of
# Reversed Pairs in Strings List
# Using list comprehension + sum()

# initializing Matrix
test_list = ["geeks", "best", "tseb", "for", "skeeg"]

# printing original list
print("The original list is : " + str(test_list))

# list comprehension for nested loop
# sum increments counts
res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len(
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))])

# printing result
print("Reversed Pairs : " + str(res))
