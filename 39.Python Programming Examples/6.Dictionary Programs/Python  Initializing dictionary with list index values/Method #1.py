# Python3 code to demonstrate working of
# Initializing dictionary with index value
# Using dictionary comprehension and enumerate()

# Initialize list
test_list = ['gfg', 'is', 'best', 'for', 'CS']

# Printing original list
print("The original list is : " + str(test_list))

# using dictionary comprehension and enumerate()
# Initializing dictionary with index value
res = {key: val for val, key in enumerate(test_list)}

# printing result
print("Constructed dictionary with index value : " + str(res))
