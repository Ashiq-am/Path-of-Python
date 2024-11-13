# Python3 code to demonstrate working of
# Keys Values equal frequency
# Using sum() + list comprehension

# initializing dictionary
test_dict = {5: 5, 8: 9, 7: 7, 1: 2, 10: 10, 4: 8}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# computing summation to get frequency
res = sum([1 for key in test_dict if key == test_dict[key]])

# printing result
print("The required frequency : " + str(res))
