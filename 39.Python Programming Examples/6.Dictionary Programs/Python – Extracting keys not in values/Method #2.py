# Python3 code to demonstrate working of
# Extracting keys not in values
# Using generator expression + set()

# initializing Dictionary
test_dict = {3 : [1, 3, 4], 5 : [1, 2], 6 : [4, 3], 4 : [1, 3]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extracting keys not in values
# Using generator expression + set()
res = list(set(test_dict) - set(ele for sub in test_dict.values() for ele in sub))

# printing result
print("The extracted keys are : " + str(res))
