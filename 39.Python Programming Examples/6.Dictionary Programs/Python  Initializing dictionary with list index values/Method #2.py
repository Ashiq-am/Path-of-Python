# Python3 code to demonstrate working of
# Initializing dictionary with index value
# Using zip() + dict() + range() + len()

# Initialize list
test_list = ['gfg', 'is', 'best', 'for', 'CS']

# Printing original list
print("The original list is : " + str(test_list))

# using zip() + dict() + range() + len()
# Initializing dictionary with index value
res = dict(zip(test_list, range(len(test_list))))

# printing result
print("Constructed dictionary with index value : " + str(res))
