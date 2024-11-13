# Python3 code to demonstrate working of
# Minimum String length
# using len() + key argument + min()

# initialize list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list : " + str(test_list))

# Minimum String length
# using len() + key argument + min()
res = len(min(test_list, key = len))

# printing result
print("Length of minimum string is : " + str(res))
