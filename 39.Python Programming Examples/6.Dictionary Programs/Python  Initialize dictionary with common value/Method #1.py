# Python3 code to demonstrate working of
# Initialize dictionary with common value
# Using list comprehension + dict()

# Initialize list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list is : " + str(test_list))

# Initialize dictionary with common value
# Using list comprehension + dict()
res = dict((sub, 4) for sub in test_list)

# printing result
print("The constructed dictionary with common value : " + str(res))
