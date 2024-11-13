# Python3 code to demonstrate working of
# Test if custom keys equal to K in dictionary
# Using all() + generator expression

# initializing dictionary
test_dict = {"Gfg" : 5, "is" : 8, "Best" : 10, "for" : 8, "Geeks" : 8}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing custom keys list
cust_keys = ["is", "for", "Geeks"]

# initializing K
K = 8

# returns true if all elements match K
res = all(test_dict[key] == K for key in cust_keys)

# printing result
print("Are all custom keys equal to K : " + str(res))
