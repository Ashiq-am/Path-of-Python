# Python3 code to demonstrate working of
# Keys with Maximum value
# Using max() + list comprehension + values()

# initializing dictionary
test_dict = {'Gfg' : 2, 'for' : 1, 'CS' : 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using max() + list comprehension + values()
# Keys with Maximum value
temp = max(test_dict.values())
res = [key for key in test_dict if test_dict[key] == temp]

# printing result
print("Keys with maximum values are : " + str(res))
