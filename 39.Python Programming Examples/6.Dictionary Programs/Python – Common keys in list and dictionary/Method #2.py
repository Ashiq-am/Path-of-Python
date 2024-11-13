# Python3 code to demonstrate working of
# Common keys in list and dictionary
# Using set() + intersection()

# initializing dictionary
test_dict = {"Gfg": 3, "is" : 5, "best" : 9, "for" : 0, "geeks" : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing test_list
test_list = ["Gfg", "best", "geeks"]

# intersection() used to get Common elements
res = set(test_list).intersection(set(test_dict))

# printing result
print("The required result : " + str(list(res)))
