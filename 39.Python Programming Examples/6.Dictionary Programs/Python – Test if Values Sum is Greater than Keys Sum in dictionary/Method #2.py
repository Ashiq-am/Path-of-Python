# Python3 code to demonstrate working of
# Test if Values Sum is Greater than Keys Sum in dictionary
# Using sum() + values() + keys()

# initializing dictionary
test_dict = {5: 3, 1: 3, 10: 4, 7: 3, 8: 1, 9: 5}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = sum(list(test_dict.keys())) < sum(list(test_dict.values()))

# printing result
print("The required result : " + str(res))
