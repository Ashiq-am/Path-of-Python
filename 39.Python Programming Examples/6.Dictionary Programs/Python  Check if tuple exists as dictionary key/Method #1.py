# Python3 code to demonstrate working of
# Check if tuple exists as dictionary key
# using in operator

# initialize dictionary
test_dict = { (3, 4) : 'gfg', 6 : 'is', (9, 1) : 'best'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initialize target tuple
tar_tup = (3, 4)

# Check if tuple exists as dictionary key
# using in operator
res = tar_tup in test_dict

# printing result
print("Does tuple exists as dictionary key ? : " + str(res))
