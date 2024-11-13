# Python3 code to demonstrate working of
# Filter Strings within ASCII range
# Using list comprehension + ord() + all()

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing ASCII range
strt_asc, end_asc = 105, 115

# checking for all characters to be in ASCII range
res = [sub for sub in test_list if all(
	ord(ele) >= strt_asc and ord(ele) <= end_asc for ele in sub)]

# printing result
print("Filtered Strings : " + str(res))
