# Python3 code to demonstrate working of
# Extract filtered Dictionary Values
# Using values()

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 2

# Extract filtered Dictionary Values
# Using values()
temp = list(test_dict.values())
res = [ele for ele in temp if ele >= K]

# printing result
print("The list of filtered values is : " + str(res))
