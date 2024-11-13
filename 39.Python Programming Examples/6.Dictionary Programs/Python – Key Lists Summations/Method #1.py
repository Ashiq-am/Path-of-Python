# Python3 code to demonstrate working of
# Key Values Summations
# Using sum() + loop

# initializing dictionary
test_dict = {'gfg': [4, 6, 8], 'is': [9, 8, 2], 'best': [10, 3, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Key Values Summations
# Using sum() + loop
for key, value in test_dict.items():
    test_dict[key] = sum(value)

# printing result
print("The summation keys are : " + str(test_dict))
