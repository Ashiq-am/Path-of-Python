# Python3 code to demonstrate working of
# Test for Empty Dictionary Value List
# Using any() + values()

# initializing dictionary
test_dict = {"Gfg" : [], "Best" : [], "is" : []}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# checking if any value is found
# using not to negate the result of any()
res = not any(test_dict.values())

# printing result
print("Are value lists empty? : " + str(res))
