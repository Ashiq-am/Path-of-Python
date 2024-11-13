# Python3 code to demonstrate working of
# Test if all Values are Same in Dictionary
# Using set() + values() + len()

# initializing dictionary
test_dict = {"Gfg" : 5, "is" : 5, "Best" : 5}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using set() to remove duplicates and check for values count
res = len(list(set(list(test_dict.values())))) == 1

# printing result
print("Are all values similar in dictionary? : " + str(res))
