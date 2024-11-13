# Python3 code to demonstrate working of
# Sort by Uppercase Frequency
# Using sorted() + lambda function


# initializing list
test_list = ["Gfg", "is", "BEST", "FoR", "GEEKS"]

# printing original list
print("The original list is: " + str(test_list))

# sorted() + lambda function used to solve problem
res = sorted(test_list, key=lambda sub: len(
	[ele for ele in sub if ele.isupper()]))

# printing result
print("Elements after uppercase sorting: " + str(res))
