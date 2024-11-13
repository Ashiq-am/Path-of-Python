# Python3 code to demonstrate working of
# Test for Ordered values from List
# Using values() + comparison operators

# initializing dictionary
test_dict = {"gfg": 4, "is": 10, "best": 11, "for": 19, "geeks": 1}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing list
sub_list = [4, 10, 11, 19, 1]

# comparing values with list
res = list(test_dict.values()) == sub_list

# printing result
print("Are values in order : " + str(res))
