# Python3 code to demonstrate working of
# Key Values Summations
# Using dictionary comprehension + sum()

# initializing dictionary
test_dict = {'gfg': [4, 6, 8], 'is': [9, 8, 2], 'best': [10, 3, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Key Values Summations
# Using dictionary comprehension + sum()
res = {key: sum(val) for key, val in test_dict.items()}

# printing result
print("The summation keys are : " + str(res))
