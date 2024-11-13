# Python3 code to demonstrate working of
# Test if custom keys equal to K in dictionary
# Using loop

# initializing dictionary
test_dict = {"Gfg": 5, "is": 8, "Best": 10, "for": 8, "Geeks": 8}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing custom keys list
cust_keys = ["is", "for", "Geeks"]

# initializing K
K = 8

# using loop to check for all keys
res = True
for key in cust_keys:
    if test_dict[key] != K:
        # break even if 1 value is not equal to K
        res = False
        break

# printing result
print("Are all custom keys equal to K : " + str(res))
