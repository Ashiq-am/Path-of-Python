# Python3 code to demonstrate working of
# Strings with all Substring Matches
# Using all() + list comprehension

# initializing list
test_list = ["gfg is best", "gfg is good for CS",
			"gfg is recommended for CS"]

# printing original list
print("The original list is : " + str(test_list))

# initializing Substring List
subs_list = ["gfg", "CS"]

# using all() to check for all values
res = [sub for sub in test_list
	if all((ele in sub) for ele in subs_list)]

# printing result
print("The extracted values : " + str(res))
