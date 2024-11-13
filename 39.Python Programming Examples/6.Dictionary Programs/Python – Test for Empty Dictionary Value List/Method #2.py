# Python3 code to demonstrate working of
# Test for Empty Dictionary Value List
# Using all() + values()

# initializing dictionary
test_dict = {"Gfg" : [], "Best" : [], "is" : []}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# checking if all keys have empty list
res = all(ele == [] for ele in list(test_dict.values()))

# printing result
print("Are value lists empty? : " + str(res))
