# Python3 code to demonstrate working of
# Check if tuple exists as dictionary key
# using get()

# initialize dictionary
test_dict = { (3, 4) : 'gfg', 6 : 'is', (9, 1) : 'best'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initialize target tuple
tar_tup = (3, 5)

# Check if tuple exists as dictionary key
# using get()
res = False
res = test_dict.get(tar_tup) != None

# printing result
print("Does tuple exists as dictionary key ? : " + str(res))
