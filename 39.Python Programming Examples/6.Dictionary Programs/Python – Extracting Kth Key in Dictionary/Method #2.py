# Python3 code to demonstrate working of
# Extracting Kth Key in Dictionary
# Using next() + iter()

# initializing dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 1

# Using next() + iter()
# Extracting Kth Key in Dictionary
test_dict = iter(test_dict)
for i in range(0, K + 1) :
	res = next(test_dict)

# printing Kth key
print("The Kth key of dictionary is : " + str(res))
