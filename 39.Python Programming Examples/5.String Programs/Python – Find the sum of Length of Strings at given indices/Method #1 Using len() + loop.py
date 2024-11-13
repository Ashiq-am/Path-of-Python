# Python3 code to demonstrate working of
# Length sum of custom indices Strings
# Using len() + loop

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks"]

# printing original lists
print("The original list is : " + str(test_list))

# initializing idx list
idx_list = [0, 1, 4]

res = 0
for idx, ele in enumerate(test_list):

	# adding length if index in idx_list
	if idx in idx_list:
		res += len(ele)

# printing result
print("Computed Strings lengths sum : " + str(res))
