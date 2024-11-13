# Python3 code to demonstrate working of
# Extracting length of longest string in list
# using len() + key argument + max()

# initialize list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list : " + str(test_list))

# Extracting length of longest string in list
# using len() + key argument + max()
res = len(max(test_list, key = len))

# printing result
print("Length of maximum string is : " + str(res))
