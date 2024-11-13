# Python3 code to demonstrate working of
# Extract Dictionary Items with Summation Greater than K
# Using filter() + lambda() + sum() + dict()

# initializing dictionary
test_dict = {"Gfg" : [6, 3, 4],
			"is" : [8, 10, 12],
			"Best" : [10, 16, 14],
			"for" : [7, 4, 3],
			"geeks" : [1, 2, 3, 4]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 15

# summation using sum(), values extracted using items()
# filter() + lambda used for computation
res = dict(filter(lambda ele: sum(ele[1]) > K, test_dict.items()))

# printing result
print("The computed dictionary : " + str(res))
