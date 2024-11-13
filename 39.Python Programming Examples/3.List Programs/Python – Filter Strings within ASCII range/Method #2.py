# Python3 code to demonstrate working of
# Filter Strings within ASCII range
# Using filter() + lambda + all() + ord()

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing ASCII range
strt_asc, end_asc = 105, 115

# checking for all characters to be in ASCII range
res = list(filter(lambda sub: all(ord(ele) >= strt_asc and ord(
	ele) <= end_asc for ele in sub), test_list))

# printing result
print("Filtered Strings : " + str(res))
