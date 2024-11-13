# Python3 code to demonstrate working of
# Replace dictionary value from other dictionary
# Using dictionary comprehension

# initializing dictionary
test_dict = {"Gfg" : 5, "is" : 8, "Best" : 10, "for" : 8, "Geeks" : 9}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing updict
updict = {"Gfg" : 10, "Best" : 17}

res = {key: updict.get(key, test_dict[key]) for key in test_dict}

# printing result
print("The updated dictionary: " + str(res))
