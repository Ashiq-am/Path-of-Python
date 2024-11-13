# Python3 code to demonstrate working of
# Extracting Kth Key in Dictionary
# Using keys() + list()

# initializing dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 1

# Using keys() + list()
# Extracting Kth Key in Dictionary
res = list(test_dict.keys())[K]

# printing Kth key
print("The Kth key of dictionary is : " + str(res))
