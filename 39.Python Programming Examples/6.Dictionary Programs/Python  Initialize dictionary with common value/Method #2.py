# Python3 code to demonstrate working of
# Initialize dictionary with common value
# Using fromkeys()

# Initialize list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list is : " + str(test_list))

# Initialize dictionary with common value
# Using fromkeys()
res = dict.fromkeys(test_list, 4)

# printing result
print("The constructed dictionary with common value : " + str(res))
