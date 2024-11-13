# Python3 code to demonstrate working of
# Initializing dictionary with list index-values
# Using dict() + enumerate()

# initializing list
test_list = ['Gfg', 'is', 'best']

# printing original list
print("The original list is : " + str(test_list))

# Initializing dictionary with list index-values
# Using dict() + enumerate()
res = dict(enumerate(test_list))

# printing result
print("The dictionary indexed as list is : " + str(res))
