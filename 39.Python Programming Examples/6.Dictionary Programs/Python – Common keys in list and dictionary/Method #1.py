# Python3 code to demonstrate working of
# Common keys in list and dictionary
# Using list comprehension

# initializing dictionary
test_dict = {"Gfg": 3, "is" : 5, "best" : 9, "for" : 0, "geeks" : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing test_list
test_list = ["Gfg", "best", "geeks"]

# using in operator to check for match
res = [ele for ele in test_dict if ele in test_list]

# printing result
print("The required result : " + str(res))
