# Python3 code to demonstrate working of
# Extract Dictionary Items with Summation Greater than K
# Using dictionary comprehension + sum()

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
res = {key: val for key, val in test_dict.items() if sum(val) > K}

# printing result
print("The computed dictionary : " + str(res))
