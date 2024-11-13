# Python3 code to demonstrate working of
# Keys with Maximum value
# Using all() + list comprehension

# initializing dictionary
test_dict = {'Gfg' : 2, 'for' : 1, 'CS' : 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using all() + list comprehension
# Keys with Maximum value
res = [key for key in test_dict if all(test_dict[temp] <= test_dict[key] for temp in test_dict)]

# printing result
print("Keys with maximum values are : " + str(res))
